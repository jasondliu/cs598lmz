import sys, threading

def run():
	while True:
		print('Hello from thread %s' % threading.currentThread())
		sys.stdout.flush()
		time.sleep(1)

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

t.join(5)
print('Main thread exiting.')
