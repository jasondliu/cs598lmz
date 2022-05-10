import sys, threading

def run():
	print("this is a test")

def main():
	t = threading.Thread(target=run)
	t.start()
	t.join()
	print("thread succeeded")

if __name__ == "__main__":
	main()
