import socket
socket.if_indextoname(1)

from socket import socket,AF_INET,SOCK_STREAM
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",4444))
s.listen(5)

while True:
	client,addr = s.accept()
	client.send(b"Hello %s\r\n" % addr[0])
	client.close()

import time
import multiprocessing

def luat_cpu(a):
	a = 0
	while True:
		a += 1
		a -= 1
	return True

if __name__ == "__main__":
	p = [0] * (multiprocessing.cpu_count())
	for i in range(0,multiprocessing.cpu_count()):
		p[i] = multiprocessing.Process(target=luat_cpu,args=(i,))
		p[i].start()

import os
os.system('dir')

f = os.popen('dir')
dir_files
