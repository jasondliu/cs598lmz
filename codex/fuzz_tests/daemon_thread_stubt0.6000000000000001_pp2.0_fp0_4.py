import sys, threading

def run():
	while True:
		for i in range(100):
			print i
			time.sleep(0.1)

t = threading.Thread(target=run)
t.start()

while True:
	sys.stdout.write('.')
	sys.stdout.flush()
	time.sleep(1)
