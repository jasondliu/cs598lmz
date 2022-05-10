import sys, threading

def run():
	print("running")
	print("thread name:", threading.current_thread().name)
	for i in range(10):
		print(i)
	print("thread name:", threading.current_thread().name)
	print("done")

def main():
	print("thread name:", threading.current_thread().name)
	t = threading.Thread(target=run, name="t")
	t.start()
	print("thread name:", threading.current_thread().name)
	t.join()
	print("thread name:", threading.current_thread().name)

if __name__ == '__main__':
	main()
