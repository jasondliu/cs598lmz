import select
# Test select.select()

# select.select() takes 3 args:
# 1. read list
# 2. write list
# 3. exception list
# It returns 3 lists:
# 1. read list
# 2. write list
# 3. exception list

# The lists are lists of file descriptors.
# select.select() blocks until one of the file descriptors is ready for I/O.

# Example:

# Create 2 pipes.
pipe1_r, pipe1_w = os.pipe()
pipe2_r, pipe2_w = os.pipe()

# Create a list of the read ends of the pipes.
read_list = [pipe1_r, pipe2_r]

# Create a list of the write ends of the pipes.
write_list = [pipe1_w, pipe2_w]

# Create an empty list for the exception list.
exception_list = []

# Call select.select() and print the results.
read_ready, write_ready, exception_ready = select.select(read_list, write_list, exception_list)
