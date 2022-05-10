import threading
threading.stack_size(67108864)

def main():
	for i in range(10):
		t = threading.Thread(target=test)
		t.start()

def test():
	for i in range(1000000):
		pass
	print(threading.current_thread().getName())

if __name__ == '__main__':
	main()
