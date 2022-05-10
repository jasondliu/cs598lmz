import threading
# Test threading daemon

def do_this(what):
	whoami(what)

def whoami(what):
	print ("Thread %s says %s " % (threading.current_thread(), what))

if __name__ == '__main__':
	whoami('I am the main Program')
	for n in range(4):
		p = threading.Thread(target=do_this,
									args=("I am function %s" % n,))
		p.start()
