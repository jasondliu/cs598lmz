import sys, threading

def run():
	for i in range(10):
		sys.stdout.write(str(i))
		time.sleep(0.1)

t = threading.Thre
