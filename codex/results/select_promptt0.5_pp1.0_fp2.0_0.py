import select
# Test select.select()

# TODO: 
# 1. Add support for Windows
# 2. Add support for Mac

# The following is a simple example of a common use of select():
# The parent process creates a pipe and then forks a child process.
# After the fork() call, both processes close the fd they don't need.
# The child writes to the pipe and the parent reads from the pipe.

# The parent process writes a string to a pipe and the child process reads it.
# The child process writes a string to a pipe and the parent process reads it.

# The pipe will be used by parent and child to communicate.
# Each end of the pipe will be an fd,
# so we can select on them.
r, w = os.pipe()

# Fork a child process.
pid = os.fork()
if pid:
    # This is the parent process. Close the child's end of the pipe.
    os.close(w)
    r = os.fdopen(r)
    # Read the child's message.
    msg = r.read()
    r.close()
    print
