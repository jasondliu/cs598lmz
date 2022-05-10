import signal
# Test signal.setitimer()
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.2)
# Test creating a pty
import pty
pty.openpty()
# Test the FD_CLOEXEC flag on the file descriptor
flags = fcntl.fcntl(1, fcntl.F_GETFD)
assert flags != -1
fcntl.fcntl(1, fcntl.F_SETFD, flags & ~fcntl.FD_CLOEXEC)
# Test creating a pipe
import os
os.pipe()
# Test difflib.IS_LINE_JUNK()
import difflib
difflib.IS_LINE_JUNK("")
# Test the LOCK_NB flag when locking a file descriptor
fcntl.LOCK_NB
# Test os.lstat()
os.lstat("/")
# Test os.major() and os.minor()
os.major(1)
os.minor(1)
# Test os.mkfifo
os.mkfifo("/tmp/mkfif
