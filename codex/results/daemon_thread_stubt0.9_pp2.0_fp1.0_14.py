import sys, threading

def run():
	while(True):
		x = input("Message: ")
		if((x == "done") or (x == "exit") or (x == "close")):
			sys.exit(0)
		elif(x == ""):
			print("Nothing")
		else:
			try:
				print("The message is: " + x)
			except:
				print("Unacceptable Character or Characters")

class Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        run()

thread = Thread()
thread.start()
