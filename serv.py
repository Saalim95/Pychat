# Server program to receive messages. ONE WAY CHAT PROGRAM.

import socket
import sys

s=socket.socket()

host='localhost'
port=1234

s.bind((host,port))

s.listen(5)

while True:
    c,a=s.accept()
    print("Got a connection from", a[0])
    while True:
        msg=c.recv(2000).decode('utf-8')    #Always receive from c. Dont forget to decode. 
        if msg=="exit":
            print("Client has gone somewhere!")
            sys.exit()
        else:
            print("Client: " + msg)
    s.close()

