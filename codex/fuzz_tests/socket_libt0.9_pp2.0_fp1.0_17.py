import socket

def Main():
	host = "192.168.1.6"
	port = 5000

	s = socket.socket()
	s.connect((host,port))

	while True:
		filename =  raw_input("Filename? ->")
		if filename != 'q':
			s.send(filename+"\n")
			data = s.recv(1024)
			if data[:6] == 'EXISTS':
				filesize = long(data[6:])
				message = raw_input("File exists,"+str(filesize)+"Bytes, download?(Y/N)? ->")
				if message == 'Y':
					s.send('OK')
					f = open('new_'+filename,'wb')
					data = s.recv(1024)
					totalRecv = len(data)
					f.write(data)
					while totalRecv < filesize and
