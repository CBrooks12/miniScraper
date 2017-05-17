import Socket
import CONFIG
import DataContainer
import sched, time

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

aCount = 0


def run_drive(runobj):
    DataContainer.update_objects(20, .001)
    for line in str(s.recv(1024)).split('\\r\\n'):
        if "PING" in line:
            s.send(line.replace("PING", "PONG"))
            break
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

        if(username == CONFIG.IDENT) and ("quit" in parts[2]):
            x = False
        print("displaying results")
        DataContainer.display_results()
    runner.enter(.1, 1, run_drive,(runobj,))


s = Socket.open_socket()
join_room(s)
runner = sched.scheduler(time.time,time.sleep)
runner.enter(.1,1,run_drive,(runner,))
runner.run()