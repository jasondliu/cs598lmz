import select
# Test select.select() by monitoring a pipe.

# Create a pipe.
r_pipe, w_pipe = os.pipe()
# Create a pipe.
r_pipe, w_pipe = os.pipe()

# Write data to the pipe.
print 'writing to pipe...'
w_pipe_fd = os.fdopen(w_pipe, 'w')
w_pipe_fd.write("testing")
w_pipe_fd.close()

# Read data from the pipe.
print 'reading from pipe...'
r_pipe_fd = os.fdopen(r_pipe, 'r')
print r_pipe_fd.read()

# Monitor the pipe for reading.
print 'monitoring pipe for reading...'
select.select([r_pipe], [], [])

# Monitor the pipe for writing.
print 'monitoring pipe for writing...'
select.select([], [w_pipe], [])

# Close the pipes.
print 'closing pipes...'
r_pipe_fd.close()
w_pipe_fd.close()

# Monitor the pipe for reading.
print
