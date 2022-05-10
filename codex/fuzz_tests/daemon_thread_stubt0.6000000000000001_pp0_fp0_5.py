import sys, threading

def run():
	print "Running"
	while True:
		print "main"
		time.sleep(1)

def run2():
	print "Running2"
	while True:
		print "main2"
		time.sleep(1)

def main():
	t = threading.Thread(target=run)
	t2 = threading.Thread(target=run2)
	t.start()
	t2.start()

if __name__ == '__main__':
	main()
