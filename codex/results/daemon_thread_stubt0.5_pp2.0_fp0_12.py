import sys, threading

def run():
	while True:
		print "hello world"


if __name__ == '__main__':
	t = threading.Thread(target=run)
	t.setDaemon(True)
	t.start()
	while True:
		pass
