import sys, threading

def run():
	i = 1
	while True:
		sys.stdout.write("\r%d" % i)
		sys.stdout.flush()
		i += 1
		time.sleep(1)
		
t = threading.Thread(target=run)
t.start()

time.sleep(5)

print "\nBye!"
