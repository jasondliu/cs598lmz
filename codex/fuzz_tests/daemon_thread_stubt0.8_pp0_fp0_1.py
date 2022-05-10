import sys, threading

def run():
	for i in xrange(1, 80):
		sys.stdout.write('\r%02d/80' % i)
		sys.stdout.flush()
		time.sleep(.05)

def main():
	th = threading.Thread(target=run)
	th.daemon = True
	th.start()

	while True:
		try:
			sys.stdin.read(1)
		except KeyboardInterrupt:
			break

if __name__ == '__main__':
	main()
