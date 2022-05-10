import sys, threading

def run():
	print 'Thread started!'
	sys.exit()

threading.Thread(target=run).start()
time.sleep(0.1)
print 'Thread finished!'
