import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for i in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# Took 0.502 seconds

# The select() function is a direct interface to the underlying operating system implementation.
# It monitors a set of file descriptors, returning whenever one or more of the file descriptors become “ready” for some class of I/O operation.
# The first three arguments to select() are sequences of “waitable objects”: either integers representing file descriptors or objects with a parameterless method named fileno() returning such an integer:
#
#     >>> import select
#     >>> import socket
#     >>> sock = socket.socket()
#     >>> def fileno(file_or_fd):
