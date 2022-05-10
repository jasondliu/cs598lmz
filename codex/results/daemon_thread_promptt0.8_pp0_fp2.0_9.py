import threading
# Test threading daemon
# https://docs.python.org/2/library/threading.html

def test_threading(name, n):
	print("Thread %s started" % name)
	for i in range(1, n+1):
		time.sleep(1)
		print("%s: %d" % (name, i))

def main():
	thread = threading.Thread(target=test_threading, name="TestThread", args=("TestThread", 5))
	thread.start()

if __name__ == "__main__":
	main()
