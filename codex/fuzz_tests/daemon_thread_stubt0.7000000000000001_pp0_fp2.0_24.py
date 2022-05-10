import sys, threading

def run():
	if len(sys.argv) < 2:
		print 'usage: %s [add|remove] name' % sys.argv[0]
		sys.exit(1)

	p = Popen(['git', sys.argv[1], sys.argv[2]], shell=True)
	thread = threading.Thread(target=p.wait)
	thread.start()
	while thread.is_alive():
		sys.stdout.write('PROGRESS %d\n' % p.poll())
		sys.stdout.flush()
		time.sleep(1)
	sys.stdout.write('PROGRESS %d\n' % p.poll())
	sys.stdout.flush()

run()
