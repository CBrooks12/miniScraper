import socket
import CONFIG

def send_message(s,message):
    s.send(bytes("PRIVMSG #" + CONFIG.IDENT + " :" + message + "\r\n", "UTF-8"))

def open_socket():
    s = socket.socket()
    print("socket initialized")
    s.connect((CONFIG.HOST, CONFIG.PORT))
    print("connecting to "+ CONFIG.HOST + " on port "+str(CONFIG.PORT))
    s.send(bytes("PASS " + CONFIG.PASS + "\r\n", "UTF-8"))
    s.send(bytes("NICK " + CONFIG.IDENT + "\r\n", "UTF-8"))
    s.send(bytes("JOIN #" + CONFIG.CHANNEL + " \r\n", "UTF-8"))
    return s