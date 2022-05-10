import threading
threading.Thread(target=main).start()

# set up socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', PORT))
s.listen(1)
print "Listening on port", PORT
conn, addr = s.accept()
print "Connected by", addr

# start main loop
while True:
	# receive message from client
	data = conn.recv(1024)
	if not data:
		break
	print "Received", data
	
	# handle message
	try:
		# parse message
		data = json.loads(data)
		command = data['command']
		args = data['args']
		
		# execute command
		if command == "start":
			print "Starting video"
			startVideo()
		elif command == "stop":
			print "Stopping video"
