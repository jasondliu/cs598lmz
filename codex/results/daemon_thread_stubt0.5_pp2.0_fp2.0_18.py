import sys, threading

def run():
	global i
	while True:
		i += 1
		print i
		time.sleep(1)

i = 0
t = threading.Thread(target=run)
t.daemon = True
t.start()

while True:
	try:
		time.sleep(1)
	except KeyboardInterrupt:
		sys.exit(0)
