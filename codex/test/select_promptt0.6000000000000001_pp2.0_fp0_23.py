import select
# Test select.select() using a pipe and stdin

import sys

print('starting...')

pipe_out, pipe_in = os.pipe()

# Set the pipe to be non-blocking
fl = fcntl.fcntl(pipe_out, fcntl.F_GETFL)
fcntl.fcntl(pipe_out, fcntl.F_SETFL, fl | os.O_NONBLOCK)

while True:
    # Wait for input from stdin & the pipe
    print('  waiting for input...')
    ready = select.select([sys.stdin, pipe_out], [], [])

    # See what input is ready
    if sys.stdin in ready[0]:
        print('  stdin is ready')
        data = sys.stdin.readline().strip()
        print('  read: %s' % data)

