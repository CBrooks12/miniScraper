import Socket
import CONFIG
import DataContainer
import sched, time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

topScores = []
xArr = []
tCounter = 0


def animate():
    global tCounter
    topScores.append(DataContainer.get_top_score())
    tCounter += 1
    xArr.append(tCounter)
    if len(xArr)>1000:
        xArr.pop(0)
        topScores.pop(0)
    ax1.clear()
    ax1.plot(xArr,topScores)


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


def run_drive(i):
    DataContainer.update_objects(40, .001)
    for line in str(s.recv(1024)).split('\\r\\n'):
        if "PING" in line:
            print("PING received")
            s.send(bytes("PONG :tmi.twitch.tv\r\n", "UTF-8"))
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

    # print("displaying results")
    # DataContainer.display_results()
    animate()
    #runner.enter(.1, 1, run_drive,(runobj,))

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

s = Socket.open_socket()
join_room(s)
ani = animation.FuncAnimation(fig, run_drive, interval=10)
plt.show()
#runner = sched.scheduler(time.time,time.sleep)
#runner.enter(.1,1,run_drive,(runner,))
#runner.run()
