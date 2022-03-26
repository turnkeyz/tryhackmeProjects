import socket 
import sys
import time

host='10.10.249.48'
port = 1337
num = 0

while 1:
	try:
		s = socket.socket()
		s.connect((host,port))
		if (port == 9765):
			break
		placeholder_port = port
		req = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % host
		s.send(req.encode())
		res = s.recv(4096)
		http_res = repr(res)
		trim = http_res[167:]
		trim = trim.replace("'",'')
		info = list(trim.split(" "))
		port = int(info[2])
		print('do what? '+info[0]+' num: '+ info[1]+', next port: '+ info[2])
		if(port != placeholder_port):
			if(info[0] == 'add'):
				num += float(info[1])
			elif(info[0] == 'subtract'):
				num -= float(info[1])
			elif(info[0] == 'multiply'):
				num *= float(info[1])
			elif(info[0] == 'divide'):
				num /= float(info[1])
		s.close()
	except:
		s.close()
		pass

print(num)