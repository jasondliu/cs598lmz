import select
# Test select.select()

import sys
from time import sleep

# Create some pipes
(read_fd1, write_fd1) = os.pipe()
(read_fd2, write_fd2) = os.pipe()

# Create a poll object
poll_object = select.poll()

# Register the pipes for input events
poll_object.register(read_fd1, select.POLLIN)
poll_object.register(read_fd2, select.POLLIN)

# Write to the pipes
os.write(write_fd1, "Hello World 1\n")
os.write(write_fd2, "Hello World 2\n")

# Wait for an event to occur
poll_result = poll_object.poll(1000)

