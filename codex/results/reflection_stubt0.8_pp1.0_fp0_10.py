fn = lambda: None
gi = (i for i in ())
fn.__code__ = ci
gi.gi_code = ci
del fn, gi, ci

__all__ = [
    "PYTHON_VERSION",
    "PYTHON_IMPLEMENTATION",

    "IS_32BIT",
    "IS_64BIT",
    "IS_PYPY",
    "IS_PYTHON",
    "IS_IRONPYTHON",
    "IS_JYTHON",
    "IS_CPYTHON",
    "IS_LOCAL",

    "LITTLE_ENDIAN",
    "BIG_ENDIAN",

    "WINDOWS",
    "LINUX",
    "DARWIN",
    "CYGWIN",

    "BITS_PER_BYTE",
    "BYTE_ORDER",
]
