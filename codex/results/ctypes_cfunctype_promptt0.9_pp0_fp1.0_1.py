import ctypes
# Test ctypes.CFUNCTYPE and ctypes.c_void_p.
# _regex is the fuzzy regex version of re.compile(), and it wraps
# regcomp() in libr.

# This test is called by test.regrtest, with test_re.py as
# the command-line argument.  We may need changes in Python's
# test.regrtest for this to work with other command-line arguments.

def mymalloc(bytes):
    pointers.append(ctypes.c_void_p())
    return pointers[-1]

def mycompile(pattern, flags):
    size = 50
    code = ctypes.c_char_p(mymalloc(size))
    errmsg = ctypes.c_char_p(mymalloc(size))
    erroffset = ctypes.c_int(0)
    c_regexp = _regex.regcomp(code, ctypes.c_char_p(pattern), erroffset, flags, errmsg, size)
    if not c_regexp:
        msg = str(errmsg[
