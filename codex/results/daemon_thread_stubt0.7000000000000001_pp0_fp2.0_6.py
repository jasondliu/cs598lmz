import sys, threading

def run():
	print 'Hello World!'
	sys.exit()

q = queue.Queue()

sys.exitfunc = run

#threading.Thread(target=run).start()

threading.Thread(target=run).join()

print 'Goodbye World!'
