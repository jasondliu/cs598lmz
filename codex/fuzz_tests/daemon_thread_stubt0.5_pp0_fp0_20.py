import sys, threading

def run():
	global flag
	flag = True
	while True:
		time.sleep(0.5)
		if flag:
			sys.stdout.write('\r'+ ' '*80 + '\r')
			sys.stdout.flush()
			sys.stdout.write('\r'+ ' '*80 + '\r')
			sys.stdout.flush()
			sys.stdout.write('\r'+ ' '*80 + '\r')
			sys.stdout.flush()
			sys.stdout.write('\r'+ ' '*80 + '\r')
			sys.stdout.flush()
			sys.stdout.write('\r'+ ' '*80 + '\r')
			sys.stdout.flush()
			sys.stdout.write('\r'+ ' '*80 + '\r')
			sys.stdout.flush()
			sys.stdout.write('\r'+
