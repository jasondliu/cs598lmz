import sys, threading

def run():
	while 1:
		try:
			number = float(raw_input())
			print number
		except ValueError, e:
			print "Fatal:", e

# With this, you can use the RawInput funtion
# like the classic input() function. This will
# be useful on threads.
def input(string):
	print string,
	return raw_input()


def main():
	t = threading.Thread(target=run)
	t.daemon = True
	t.start()
	while 1:
		try:
			# do work
			print "Loop", threading.current_thread().ident, ":", threading.current_thread().name
			pass
		except KeyboardInterrupt, e:
			print "Fatal:", e
