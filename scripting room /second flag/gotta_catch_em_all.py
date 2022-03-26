import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = ''
port = 80
s.connect((host,port))