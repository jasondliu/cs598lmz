import sys, threading

def run():
	for i in range(3):
		sys.stdout.write('Hello world from child, %s\n' % i)
		sys.stdout.flush()
		time.sleep(1)

def test():
	t = threading.Thread(target=run)
	t.start()
	while True:
		line = sys.stdin.readline()[:-1]
		print('Parent %s got "%s" at %s' % (os.getpid(), line, time.time()))
		sys.stdout.flush()

if __name__ == '__main__':
	test()
