import sys, threading

def run():
	sys.exit(subprocess.call('py.test -m "not manual"', shell=True))

t1 = threading.Thread(target=run)
t1.start()

t1.join(timeout=30)
if t1.is_alive():
	print "tests still running after 30 seconds, aborting"
	os._exit(1)
