import sys, threading

def run():
	for i in range(10):
		print "hi from thread"

def main():
	for i in range(10):
		print "hi from main"

if __name__ == '__main__':
	thread = threading.Thread(target=run)
	thread.start()
	main()
