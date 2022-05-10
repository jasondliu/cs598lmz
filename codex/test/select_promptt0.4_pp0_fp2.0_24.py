import select
# Test select.select()

# The select.select() function takes three lists of objects:
#   - the first list contains objects to be monitored for being ready to read
#   - the second list contains objects to be monitored for being ready to write
#   - the third list contains objects to be monitored for errors
# The function will block until one or more of the objects in the lists are ready.
# The return value is a tuple of three lists:
#   - the first list contains objects that are ready to read
#   - the second list contains objects that are ready to write
#   - the third list contains objects that have errors

# The select.select() function can be used with sockets, pipes and files.

# Create a pipe
pipe_read, pipe_write = os.pipe()

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 0))
sock.listen(1)

# Create a file
file = open("/tmp/test.txt", "w")

