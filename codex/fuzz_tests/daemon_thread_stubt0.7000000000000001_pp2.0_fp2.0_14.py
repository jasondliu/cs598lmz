import sys, threading

def run():
	print("Thread")

def main():
	t = threading.Thread(group=None, target=run, name="thread", args=(), kwargs=None, verbose=None)
	t.start()
	print("Main")

if __name__ == "__main__":
	main()
	sys.exit(0)
