import select
# Test select.select()

# select.select() takes 3 lists of file descriptors (input, output, error)
# and a timeout. It returns 3 lists of the file descriptors that are ready
# for reading, writing, and erroring.

# Create a pipe
r, w = os.pipe()

# Make the read end non-blocking
fl = fcntl.fcntl(r, fcntl.F_GETFL)
fcntl.fcntl(r, fcntl.F_SETFL, fl | os.O_NONBLOCK)

# Write some data to the pipe
os.write(w, 'hello')

# Wait for the pipe to be ready for reading
rlist, wlist, xlist = select.select([r], [], [], 5)

# Read the data
print os.read(r, 5)

# Close the file descriptors
os.close(r)
os.close(w)
