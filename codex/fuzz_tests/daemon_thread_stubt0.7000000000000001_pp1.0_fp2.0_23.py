import sys, threading

def run():
	global count, lock
	while True:
		receive = s.recv(1024)
		if not receive:
			break
		count = count + 1
		print receive
		lock.release()

count = 0
lock = threading.Lock()

if len(sys.argv) != 3:
	print "Usage: client.py <IP> <Port>"
	sys.exit()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], int(sys.argv[2])))

thread = threading.Thread(target = run)
thread.start()

while True:
	lock.acquire()
	if count > 0:
		send = raw_input()
		s.send(send)
		if send == "quit" or send == "disconnect":
			break;
		count = count - 1

s.close()
