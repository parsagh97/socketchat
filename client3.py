import socket
from encrypt import *
host = "127.0.0.1"
port = 5058
s = socket.socket()
s.connect((host, port))
msg = input("you: ")
while msg != 'good bye':
    msg = encrypt(msg)
    s.send(msg.encode('ascii'))
    data = s.recv(1024)
    data = data.decode('ascii')
    data = decrypt(data)
    print("server: " + str(data))
    msg = input("you: ")
s.close()