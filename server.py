import socket
s = socket.socket()
print('socket created')
s.bind(('192.168.29.233',9989))
s.listen(3)
print('waiting for connections')
while True:
    c,addr = s. accept()
    name = c.recv(1024).decode()
    age = c.recv(1024).decode()
    print('connected with',addr,name)
    c.send(bytes('welcome to my world','utf-8'))
    c.close()
