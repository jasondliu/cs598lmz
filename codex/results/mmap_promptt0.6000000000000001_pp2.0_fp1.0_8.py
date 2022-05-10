import mmap
# Test mmap.mmap to see if it's available
try:
    mmap.mmap(0, 1, access=mmap.ACCESS_READ)
except (AttributeError, EnvironmentError):
    mmap = None
else:
    mmap.mmap(0, 1, access=mmap.ACCESS_READ)

# POSIX allows SIGPIPE to be ignored, but not all platforms make Python's
# signal.SIGPIPE ignoreable (Python bug #1652).
# Catch the SIGPIPE if possible.
try:
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
except ValueError:
    pass

# The default working directory is os.getcwd(), but the default cwd
# for new subprocesses is os.environ['HOME'].  We must ensure that the
# two are in sync.
home = os.environ.get('HOME')
if home:
    home = os.path.realpath(home)
    if os.getcwd() != home:
        os.chdir(home)

