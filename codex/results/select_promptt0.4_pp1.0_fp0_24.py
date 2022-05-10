import select
# Test select.select()

# Create a pipe
r, w = os.pipe()

# Create non-blocking pipe
flags = fcntl.fcntl(r, fcntl.F_GETFL)
fcntl.fcntl(r, fcntl.F_SETFL, flags | os.O_NONBLOCK)

# Write to pipe
os.write(w, 'hello world')

# Select on pipe for reading
rlist, wlist, xlist = select.select([r], [], [])

# Read from pipe
print os.read(r, 100)
