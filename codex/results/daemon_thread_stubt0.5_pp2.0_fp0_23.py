import sys, threading

def run():
	a = raw_input()
	print a

def main():
	t1 = threading.Thread(target=run)
	t2 = threading.Thread(target=run)
	t1.start()
	t2.start()
	t1.join()
	t2.join()

main()
