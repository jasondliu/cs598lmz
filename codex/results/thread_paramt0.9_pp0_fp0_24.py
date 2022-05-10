import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Thread-2 wrote this\n')).start()
threading.Thread(target=lambda: sys.stdout.write('Thread-3 wrote this\n')).start()
#Thread-2 wrote this
#Thread-3 wrote this

# - redirecting writes to extra file descriptors
# - mapping extra file descriptors to same file object
# - remember that print() writes to a file implicitly
# - using the extra file descriptor in redirection
# - redirect the write file descriptor to a subprocess
#   - echo, tee, cat, etc.
# - NOTE: the write file descriptor is flushed each line!
#         Otherwise only flushed when full or closed.
import os

# keep a private pipe
fd3, fd4 = os.pipe()

# redirect stdout 
os.dup2(fd4, 1)
os.close(fd4)

# map write file descriptor to out_fd
fd5 = os.fdopen(fd3, 'w')
out_fd = os.fdopen(3, 'w')

# map write file descriptor to both
