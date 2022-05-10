import sys, threading

def run():
	while True:
		print("{}\n".format(threading.current_thread()), file=sys.stdout)
		threading._sleep(1)

def task(n):
	while n > 0:
		print("{}: {}\n".format(threading.current_thread(), n), file=sys.stdout)
		n -= 1
		threading._sleep(1)

if __name__ == '__main__':
	t = threading.Thread(target=run, daemon=True)
	t.start()
	t2 = threading.Thread(target=task, args=(3,))
	t3 = threading.Thread(target=task, args=(5,))
	t2.start()
	t3.start()
