import select
# Test select.select with a pipe and a timeout

import select, os, time

# Create a pipe
r, w = os.pipe()

# Create a reader and writer from the pipe
r = os.fdopen(r, 'rb', 0)
w = os.fdopen(w, 'wb', 0)

# Empty the pipe
data = r.read()
assert data == ""

# Wait until the pipe is readable
t1 = time.time()
t = select.select([r], [], [], 3.0)
t2 = time.time()
assert t == ([r], [], [])
assert t2-t1 >= 3.0, "timeout not respected got %s" % (t2-t1,)

# Write something to the pipe
w.write("hello world")
w.flush()

# Wait until the pipe is readable
t1 = time.time()
t = select.select([r], [], [], 3.0)
t2 = time.time()
assert t == ([r], [], [])
assert t2-t1 < 3.0,
