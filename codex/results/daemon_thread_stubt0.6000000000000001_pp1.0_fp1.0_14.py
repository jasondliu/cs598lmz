import sys, threading

def run():
	try:
		threading.Thread(target=send).start()
		threading.Thread(target=receive).start()
	except:
		print("Error: unable to start thread")

def send():
	global s, host, port
	while True:
		try:
			data = input()
			s.send(data.encode('utf-8'))
		except:
			print("Error: unable to send")
			sys.exit()

def receive():
	global s, host, port
	while True:
		try:
			data = s.recv(1024).decode('utf-8')
			if not data:
				print("Disconnected")
				sys.exit()
			else:
				print(data)
		except:
			print("Error: unable to receive")
			sys.exit()

if __name__ == "__main__":
	s = socket.socket(socket.AF
