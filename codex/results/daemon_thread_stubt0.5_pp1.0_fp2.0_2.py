import sys, threading

def run():
	for i in range(10):
		time.sleep(5)
		print('threading {0}'.format(i))

if __name__ == '__main__':
	t = threading.Thread(target=run)
	t.start()

	while True:
		print('main threading')
		time.sleep(1)
		sys.stdout.flush()
