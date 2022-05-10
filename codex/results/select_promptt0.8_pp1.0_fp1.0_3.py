import select
# Test select.select(), with and without signal handling

import os, select, signal, sys, time

signal.signal(signal.SIGINT, signal.SIG_IGN)

print "Running select test"

stdin = sys.stdin.fileno()
stdout = sys.stdout.fileno()

# Set non-blocking reads
fcntl.fcntl(stdin, fcntl.F_SETFL, os.O_NDELAY)

# Make the output buffer bigger (2048 bytes)
old = fcntl.fcntl(stdout, fcntl.F_GETFL)
fcntl.fcntl(stdout, fcntl.F_SETFL, old | os.O_NDELAY)

# main loop
while 1:
    time.sleep(1)
    print "."
    ready = select.select([sys.stdi
