# Client
#Default Access

import socket as sock
import 

s=sock.socket(sock.AF_INET, sock.SOCK_STREAM)

host='localhost'
port=1234
msg=''

ip=sock.gethostbyname(host)

s.connect((ip, port))

print("Connected to Server")

while (msg!='exit'):
    msg=input("You: ")

    s.sendall(msg.encode('utf-8'))


s.close()
