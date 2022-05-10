import sys, threading

def run():
	while True:
		print "Hello, World!"
		time.sleep(1)

t = threading.Thread(target=run)
t.daemon = True
t.start()

sys.stdin.read(1)
