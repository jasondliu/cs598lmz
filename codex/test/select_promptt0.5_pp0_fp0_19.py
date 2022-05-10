import select
# Test select.select()

# Create non-blocking sockets
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set them to non-blocking
s1.setblocking(0)
s2.setblocking(0)
s3.setblocking(0)

# Connect them
s1.connect(('www.google.com', 80))
s2.connect(('www.yahoo.com', 80))
s3.connect(('www.bing.com', 80))

# Create the list of sockets to check for data
read_list = [s1, s2, s3]
write_list = []
error_list = []

# Check for data
readable, writable, errored = select.select(read_list, write_list, error_list)

# Print out sockets with data
print(readable)

# Close sockets
s1
