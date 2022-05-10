import sys, threading

def run():
	for i in xrange(10):
		print "hello"

thread = threading.Thread(target=run)
thread.start()

thread.join()
