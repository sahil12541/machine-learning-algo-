import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip_add = "172.20.10.5"
port = 1234
complete = (ip_add, port)
massage =input("kya msg kroge")
encode_mgs=massage.encode('ascii')
s.sendto(encode_mgs,complete)
