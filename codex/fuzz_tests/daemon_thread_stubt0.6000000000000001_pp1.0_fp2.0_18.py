import sys, threading

def run():
	sys.stdout.write('Running\n')
	sys.stdout.flush()
	t = threading.current_thread()
	while getattr(t, 'running', True):
		print('thread %s' % t.name)
		sys.stdout.flush()
		time.sleep(1)
	print('thread %s stopped' % t.name)
	sys.stdout.flush()

def test():
	t = threading.Thread(target=run)
	t.start()
	time.sleep(3)
	t.running = False
	t.join()

if __name__ == '__main__':
	test()
