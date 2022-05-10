import sys, threading

def run():
	sys.stdout.write("\n")
	sys.stdout.flush()
	return

def main(argv):
	sys.stdout.write("\n")
	sys.stdout.flush()
	for i in range(0,10):
		threading.Timer(i, run).start()
	return

if __name__ == "__main__":
	main(sys.argv)
