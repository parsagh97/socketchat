import socket
from encrypt import *
host = "127.0.0.1"
port = 5058
s = socket.socket()
s.bind((host, port))
s.listen(1)
c, add = s.accept()
print("client: " + str(add))
while True:
    data = c.recv(1024)
    if not data:
        break
    data = data.decode('ascii')
    data = decrypt(data)
    print ("client:" + str(data))
    data = input("you: ")
    data = encrypt(data)
    c.send(data.encode('ascii'))
c.close()