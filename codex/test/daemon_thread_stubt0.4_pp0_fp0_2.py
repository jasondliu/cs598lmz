import sys, threading

def run():
	while True:
		sys.stdout.write(".")
		sys.stdout.flush()
		time.sleep(0.5)

if __name__ == "__main__":
	thread = threading.Thread(target=run)
	thread.daemon = True
	thread.start()
