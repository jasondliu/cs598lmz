import select
# Test select.select()
#

# Interrupt test.
# Since select.select() only returns when an I/O event occurs,
# the only way of forcing it to return is an alarm signal
# or an I/O event.

exit(0)
def handler(signum, frame):
    print 'handler called with signum = ', signum

old = signal.signal(signal.SIGALRM, handler)
signal.alarm(10)
try:
    ready = select.select([], [], [])
    print ready
finally:
    signal.alarm(0)
    signal.signal(signal.SIGALRM, old)

# Polling test.
# Create a subprocess, let it run for a couple of seconds,
# then check for data on the pipe.  The process should have
# produced some output by the second select().

print 'starting subprocess'
f = os.popen('sleep 2; echo "subprocess"')
pollster = select.poll()
pollster.register(f)
print 'starti
