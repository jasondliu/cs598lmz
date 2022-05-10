import sys, threading

def run():
	while True:
		print("hello 1")
		sys.stdout.flush()
		time.sleep(1)
		
t1 = threading.Thread(target=run)
t1.daemon = True
t1.start()

while True:
	print("hello 2")
	sys.stdout.flush()
	time.sleep(1)
