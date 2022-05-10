import _struct
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 80))
s.listen(5)
while True:
	client, address = s.accept()
	print "Connection from: " + str(address)
	client.send('HTTP/1.1 200 OK\n')
	client.send('Content-Type: text/html\n')
	client.send('\n') # header and body should be separated by additional newline
	# f = open('index.html', 'r')
	# data = f.readlines()
	# for line in data:
	# 	client.send(line)
	client.send('<html><body>Hello world!</body></html>')
	client.close()
