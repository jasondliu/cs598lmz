import select
# Test select.select

# First, create some pipes

r, w = os.pipe()

# Create non-blocking file descriptors

r = os.fdopen(r, 'rb', 0)
w = os.fdopen(w, 'wb', 0)

# Create a poll object

p = select.poll()

# Register the pipes to be watched for input

p.register(r, select.POLLIN)

# Write some data to the pipe

w.write('hello')
w.flush()

# Wait for input on the pipe

