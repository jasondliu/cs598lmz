import sys, threading

def run():
	sys.exit(CloudFS().main(sys.argv))

#Invoking the main function if this is the main thread
threading.Thread(target=run).start()
