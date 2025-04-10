import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add = "172.20.10.5"
port = 1234
complete = (ip_add, port)
s.bind(complete)
while True:
    msg=s.recvfrom(1024)
    msg=msg[0].decode('ascii')
    print(msg)