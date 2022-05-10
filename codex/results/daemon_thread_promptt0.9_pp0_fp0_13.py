import threading
# Test threading daemon
class AsyncWrite(threading.Thread):
	def __init__(self,text,out):
		threading.Thread.__init__(self)
		self.text = text
		self.out = out
	def run(self):
		f = open(self.out,"a")
		f.write(self.text+"\n")
		f.close() 
		time.sleep(2)
		print("Finished Background File Write to "+self.out)

def Main():
	message = input("Enter a string to be store:")
	background = AsyncWrite(message,"out.txt")
	background.start()
	print("Main program continues to run in foreground")
	#without join() , the program finished before background thread finishes
	background.join() 
	print("Program waited until the background thread was done!")


if __name__ == "__main__": Main()



### Threading Lock
import threading
tLock = threading.Lock()

def timer(name,delay,repeat):
	print
