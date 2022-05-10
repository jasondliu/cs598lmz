import sys, threading

def run():
    print('Read stdin')
    for line in sys.stdin:
        print('Entering thread, wrote: %s' % line)
    print('Exiting thread')

thread = threading.Thread(target=run)
thread.start()

print('Started thread')
thread.join()
print('Joined thread')

# Output:
# Started thread
# Read stdin
# Entering thread, wrote: This is a test
# Entering thread, wrote: of the emergency broadcast system
# Joined thread
# Exiting thread

# Final output:
# Started thread
# Read stdin
# Entering thread, wrote: This is a test
# Entering thread, wrote: of the emergency broadcast system
# Joined thread
# Exiting thread

# The interesting part of the output is that we saw the output from
# test.py interleaved with the output from thread_stdin.py. That’s
# because the main thread was paused at thread.join() while test.py
# and thread_stdin.py were both writing to stdout and stderr.

# Final
