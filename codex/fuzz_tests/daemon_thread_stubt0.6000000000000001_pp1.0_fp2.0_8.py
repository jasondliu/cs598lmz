import sys, threading

def run():
	print("Thread started")
	time.sleep(2)
	print("Thread ended")

def main():
	print("Main started")
	t = threading.Thread(target=run)
	t.start()
	print("Main ended")

if __name__ == '__main__':
	main()
