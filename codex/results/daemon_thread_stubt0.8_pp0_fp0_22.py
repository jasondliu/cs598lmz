import sys, threading

def run():
	while True:
		line = sys.stdin.readline()
		print "You entered: " + line.strip()
		threading.Timer(1, run).start()
run()
