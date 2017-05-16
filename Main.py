import Socket

def loadingComplete(line):
    if("End of /NAMES list" in line):
        return False
    else:
        return True

def joinRoom(s):
    readbuffer = ""
    Loading = True
    while Loading:
        readbuffer = readbuffer + str(s.recv(1024))
        print(readbuffer)
        temp = readbuffer.split('\\n')
        print(temp)
        readbuffer = temp.pop()

        for line in temp:
            Loading = loadingComplete(line)
    Socket.send_message(s, "Successfully joined chat")


s = Socket.open_socket()
joinRoom(s)

x = True
while x:
    for line in str(s.recv(1024)).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue

        #if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
        #    message = parts[2][:len(parts[2])]

        username = parts[1].split("!")[0]

        print(username + ": " + parts[2])
        if("Hey" in parts[2]):
           Socket.send_message(s,"Hello " +username)
        if((username == "latv_potato") and ("quit" in parts[2])):
            x = False