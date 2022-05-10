import sys, threading

def run():
	print('Thread {} is running...'.format(threading.current_thread().name))
	n = 0
	while n < 5:
		n = n + 1
		print('Thread {} >>> {}'.format(threading.current_thread().name, n))
		time.sleep(1)
	print('Thread {} is end'.format(threading.current_thread().name))

if __name__ == '__main__':
	print('Thread {} is running...'.format(threading.current_thread().name))
	t = threading.Thread(target=run, name='SonThread')
	t.start()
	t.join()
	print('Thread {} is end'.format(threading.current_thread().name))
