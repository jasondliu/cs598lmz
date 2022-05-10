import sys, threading

def run():
	while True:
		print 'Hello!'
		time.sleep(10)

def main():
	k = threading.Thread(target=run)
	k.start()
	
	while True:
		print 'Main Thread'
		time.sleep(5)

if __name__ == "__main__":
	main()
