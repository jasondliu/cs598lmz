import sys, threading

def run():
	print 'run'
	return

def main(argv):
	thread = threading.Thread(target=run)
	thread.start()
	return

if __name__ == '__main__':
	main(sys.argv)
