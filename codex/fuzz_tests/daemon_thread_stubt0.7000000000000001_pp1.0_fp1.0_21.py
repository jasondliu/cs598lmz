import sys, threading

def run():
	start = time.time()
	sys.stdout.write("\r%d%%" % 0)
	sys.stdout.flush()
	for i in range(1, 101):
		time.sleep(0.01)
		sys.stdout.write("\r%d%%" % i)
		sys.stdout.flush()
	end = time.time()
	print("\nTotal time: %.2f seconds" % (end - start))

run()
