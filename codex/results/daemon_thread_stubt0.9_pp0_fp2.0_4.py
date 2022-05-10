import sys, threading

def run():
	try:
		while True:
			yield threading.Event().wait()
	except GeneratorExit:
		print 'Hello'


r = run()
r.next()
r.close()
