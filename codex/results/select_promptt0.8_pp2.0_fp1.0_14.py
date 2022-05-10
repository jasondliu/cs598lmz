import select
# Test select.select()
# Notice:
#   1. select will modify the param 'readable' and 'writable',
#      and it only waits for 'readable'
#   2. select doesn't work with fd 0, it seems to be blocked

# Prepare pipes
r, w = os.pipe()

# Prepare input
print >> sys.stderr, "Ready to receive data thru pipe ..."

# Prepare output
print >> sys.stderr, "Ready to send data to stdout ..."

# Start
print >> sys.stderr, "Start select() ..."
readable, writable, exceptional = select.select([r, sys.stdin], [sys.stdout], [])
for fd in readable:
    if fd == r:
        data = os.read(r, 1024)
        print >> sys.stderr, "Read from pipe:", data
    elif fd == sys.stdin:
        data = sys.stdin.readline()
        print >> sys.stderr, "Read from stdin:", data
        os.write(w, data)
