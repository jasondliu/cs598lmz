import _struct
import _wrapper

# The following two functions are used to ensure that a stream argument is
# converted to a file descriptor.
def _fileobject(f):
    if isinstance(f, file):
        return f.fileno()
    else:
        return f

def _fileobject_closed_ok(f):
    if isinstance(f, file):
        return f.fileno()
    else:
        return f

# Helper functions to perform the corresponding CPython ioctl() calls.
def _ioctl_int(fd, op, arg=0):
    buf = _struct.pack('iL', arg, 0)
    return _fcntl.ioctl(fd, op, buf)

def _ioctl_string(fd, op, arg=''):
    buf = _struct.pack('i%ds' % len(arg), len(arg), arg)
    return _fcntl.ioctl(fd, op, buf)

class _error(Exception):
    pass

error = _error

class Termios:
    # Create new Termios
