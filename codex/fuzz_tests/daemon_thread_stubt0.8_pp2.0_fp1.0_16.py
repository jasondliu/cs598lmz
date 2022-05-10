import sys, threading

def run():
	while True:
		data = sys.stdin.readline()
		if not data:
			break
		print >> sys.stderr, "From parent:", data
		print data[:-1] + " Child"

thread = threading.Thread(target=run)
thread.start()
thread.join()
print >> sys.stderr, "Child done"

#def run():
#	while True:
#		data = sys.stdin.readline()
#		if not data:
#			break
#		print >> sys.stderr, "From parent:", data
#		print data[:-1] + " Child"
#
#run()
#print >> sys.stderr, "Child done"
