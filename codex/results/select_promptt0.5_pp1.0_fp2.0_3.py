import select
# Test select.select()

def slow_systemcall():
    select.select([], [], [], 0.1)

start = time.time()
for _ in range(5):
    slow_systemcall()
end = time.time()
print('Took %.3f seconds' % (end - start))

# The cost of 5 system calls is roughly the same as a single system call.

# The select() function is a direct interface to the Unix select() system call.
# It monitors sockets, open files, and pipes (anything with a fileno() method
# that returns a valid file descriptor) until they become readable or writable
# or a communication error occurs. The first three arguments are sequences of
# “waitable objects”: either integers representing file descriptors or objects
# with a parameterless method named fileno() that returns such an integer:

# If the time limit is omitted the function blocks until at least one file
# descriptor is ready. A time limit of zero specifies a poll and never blocks.
# In all cases a tuple is returned that lists which sockets are ready.

# The select() function supports a third
