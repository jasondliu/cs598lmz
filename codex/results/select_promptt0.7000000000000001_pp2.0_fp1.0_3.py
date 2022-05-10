import select
# Test select.select()
# Timeout in seconds
timeout = 2
# Default poller
# Read, Write, Error
rlist, wlist, elist = select.select([sys.stdin], [], [], timeout)
if rlist:
    s = sys.stdin.readline()
    print("You entered", s)
else:
    print("Timeout")
