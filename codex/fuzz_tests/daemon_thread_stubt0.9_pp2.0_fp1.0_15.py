import sys, threading

def run():
	sys.stdout.write('Hello from thread %s\n' % threading.current_thread())

if __n
