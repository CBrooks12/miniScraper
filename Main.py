import Socket
import CONFIG
import DataContainer


def loading_complete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True


def join_room(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + str(s.recv(1024))
        print(readbuffer)
        temp = readbuffer.split('\\n')
        print(temp)
        readbuffer = temp.pop()

        for line in temp:
            Loading = loading_complete(line)
    Socket.send_message(s, "Successfully joined chat")


s = Socket.open_socket()
join_room(s)

x = True
aCount = 0

while x:
    aCount += 1
    DataContainer.update_objects(20, .001)
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue

        username = parts[1].split("!")[0]
        #print(username + ": " + parts[2])
        splitMessage = parts[2].split(' ')
        uniqueWordsList = []
        for word in splitMessage:
            if word not in uniqueWordsList:
                uniqueWordsList.append(word)
        for word in uniqueWordsList:
            DataContainer.add_to_container(word)

        if("Hey" in parts[2]):
           Socket.send_message(s,"Hello " +username)

        if(username == CONFIG.IDENT) and ("quit" in parts[2]):
            x = False

    if aCount > 10:
        aCount = 0
        print("displaying results")
        DataContainer.display_results()
