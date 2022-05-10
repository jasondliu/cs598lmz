import sys, threading

def run():
	fo = open(sys.argv[2], "wb")
	while True:
		line = sys.stdin.readline()
		fo.write(line)
		fo.flush()
		print line

t = threading.Thread(target = run)
t.setDaemon(True)
t.start()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect((sys.argv[1], 50000))

while True:
	line = s.recv(1000000)
	sys.stdout.write(line)
	sys.stdout.flush()
