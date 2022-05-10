import sys, threading

def run():
	run_time = 0
	while run_time < 5:
		sys.stdout.write('\r')
		sys.stdout.flush()
		sys.stdout.write('|')
		sys.stdout.flush()
		time.sleep(1)
		sys.stdout.write('\r')
		sys.stdout.flush()
		sys.stdout.write('/')
		sys.stdout.flush()
		time.sleep(0.5)
		sys.stdout.write('\r')
		sys.stdout.flush()
		sys.stdout.write('-')
		sys.stdout.flush()
		time.sleep(0.5)
		sys.stdout.write('\r')
		sys.stdout.flush()
		sys.stdout.write('\\')
		sys.stdout.flush()
		time.sleep(0.5)
		run_time += 1

threading.Thread(target = run
