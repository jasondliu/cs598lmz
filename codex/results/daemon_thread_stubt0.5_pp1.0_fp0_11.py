import sys, threading

def run():
	while True:
		sys.stdout.write('.')
		time.sleep(1)

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

time.sleep(10)
