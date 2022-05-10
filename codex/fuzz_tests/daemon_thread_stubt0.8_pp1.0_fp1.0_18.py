import sys, threading

def run():
	try:
		for i in range(100):
			sys.stdout.write('%s\n' % threading.currentThread().getName())
			sys.stdout.flush()
	finally:
		print "Goodbye"

t = threading.Thread(name='my-thread', target=run)
t.setDaemon(True)
t.start()
t.join()
