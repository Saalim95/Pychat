# Client


import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host='localhost'
port=1234
msg=''

ip=socket.gethostbyname(host)

s.connect((ip, port))

print("Connected to Server")

while (msg!='exit'):
    msg=input("Client: ")

    s.sendall(msg.encode('utf-8'))

    #reply=s.recv(4096)

    #print(reply)

s.close()
