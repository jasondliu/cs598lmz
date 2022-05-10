import sys, threading

def run():
	print "Running thread"

	t1 = threading.Thread(target=scan)
	t1.start()
	
	userInput = ""
	while userInput != "exit\n":
		userInput = raw_input("")
	
	os.kill(os.getpid(), signal.SIGKILL)

def scan():
	print "Scanning..."
	while (1):
		print "Scan"
		time.sleep(5)

run()
