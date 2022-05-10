import sys, threading

def run():
	while 1:
		line = sys.stdin.readline()
		if not line:
			return
		print(line, end='')
		sys.stdout.flush()

thread = threading.Thread(target=run)
thread.start()
