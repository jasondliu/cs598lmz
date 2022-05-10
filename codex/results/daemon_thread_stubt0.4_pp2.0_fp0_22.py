import sys, threading

def run():
	for i in range(10):
		print(i)
		time.sleep(1)

if __name__ == '__main__':
	thread = threading.Thread(target=run)
	thread.start()

	while True:
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			sys.exit()
