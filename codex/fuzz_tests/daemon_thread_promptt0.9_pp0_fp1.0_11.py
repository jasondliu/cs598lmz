import threading
# Test threading daemon mode

def workerB():
	print "workerB start"
	t = threading.Timer(1, workerB)
	t.setDaemon(True)
	t.start()

def workerA():
	print "workerA start"
	t = threading.Timer(1, workerB)
#	t.setDaemon(True)
	t.start()
	threading.Timer(5, workerA).start()

if __name__ == '__main__':
	workerA()
