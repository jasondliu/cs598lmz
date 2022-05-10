import select
# Test select.select()

# Create a pipe
pipe_1, pipe_2 = os.pipe()

# Create non-blocking pipe file descriptors
pipe_1_nb = fcntl.fcntl(pipe_1, fcntl.F_SETFL, os.O_NONBLOCK)
pipe_2_nb = fcntl.fcntl(pipe_2, fcntl.F_SETFL, os.O_NONBLOCK)

# Write to pipe
os.write(pipe_2, b'Hello')

# Poll the pipe
poll = select.poll()
poll.register(pipe_1_nb, select.POLLIN)

# Wait for data to be available
events = poll.poll(1) # Timeout after 1 second

# Read from pipe
print(os.read(pipe_1_nb, 1024))

# Clean up
os.close(pipe_1)
os.close(pipe_2)

# Create a pipe
pipe_1, pipe_2 = os.pipe()

# Create non-blocking pipe file descript
