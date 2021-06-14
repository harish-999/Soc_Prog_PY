import socket
c = socket.socket()
c.connect(('192.168.29.233',9989))
name = input('enter the name:')
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())
