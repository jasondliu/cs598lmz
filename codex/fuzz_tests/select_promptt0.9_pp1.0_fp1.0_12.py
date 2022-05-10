import select
# Test select.select usage on stdin.
print "Testing select on stdin...",
fileno = sys.stdin.fileno()
readfds = select.select([fileno], [], [], 0)[0]
if fileno in readfds:
	print "ERROR"
print "OK"

# Test select on bytes from stdin.
print "Testing select on stdin bytes...",
fileno = sys.stdin.buffer.fileno()
readfds = select.select([fileno], [], [], 0)[0]
if not fileno in readfds:
	print "ERROR"
print "OK"
