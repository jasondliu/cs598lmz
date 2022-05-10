import sys, threading

def run():
	#while True:
		#sys.stdout.write(".")
		#sys.stdout.flush()
		#time.sleep(1)
	#return
	
	while True:
		#sys.stdout.write(".")
		#sys.stdout.flush()
		time.sleep(1)
		
		#print "Alive", threading.activeCount()
		
		#if threading.activeCount() == 1:
		#	break
		
		if threading.activeCount() == 1:
			break
		
		#if not threading.enumerate():
		#	break
		
		#if not threading.enumerate():
		#	break
	
	print "Exiting"

t = threading.Thread(target=run)
t.setDaemon(True)
t.start()

def f():
	print "Hello"

f()

#time.sleep(2)

sys.exit(0)
