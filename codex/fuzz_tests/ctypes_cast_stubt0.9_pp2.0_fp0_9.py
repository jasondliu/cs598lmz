import ctypes
ctypes.cast(ctypes.c_char_p('x' * 10), ctypes.c_void_p).value

def index_of(char, s):
    """Return the index of char in s, or len(s) if char not in s."""
    for i in xrange(len(s)):
        if s[i] == char:
            return i
    return len(s)

def str_to_int(s):
    """Convert a string of digits to an int, or None if s is unparseable."""
    result = 0
    for c in s:
        if not c.isdigit():
            return None
        result = result * 10 + int(c)
    return result

def eprint(*args, **kwargs):
    """Print to stderr."""
    import sys
    print(*args, file=sys.stderr, **kwargs)

def perror(*args):
    """Print to stderr."""
    import sys
    print(*args, file=sys.stderr)

def error(exit_
