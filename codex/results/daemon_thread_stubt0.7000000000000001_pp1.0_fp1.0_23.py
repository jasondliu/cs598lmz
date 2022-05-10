import sys, threading

def run():
	sys.stdout.write("%s\n" % threading.currentThread().getName())
	sys.stdout.flush()
	return

if __name__ == '__main__':
	for i in xrange(10):
		t = threading.Thread(target = run)
		t.start()
