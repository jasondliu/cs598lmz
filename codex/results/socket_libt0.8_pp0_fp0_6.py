import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))

msg = ""
while msg != "q":
	msg = raw_input("Message ")
	s.send(msg)
	print s.recv(1024)

s.close()
