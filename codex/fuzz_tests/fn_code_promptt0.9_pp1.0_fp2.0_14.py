fn = lambda: None
# Test fn.__code__ and fn.__closure__
RT.__code__, RT.__closure__ = RT.__code__, RT.__closure__

# Configure template mapping from RT to TYPES
TEMPLATES = {'%c': int, '%d': int, '%u': int, '%ld': int, '%lu': int,
             '%lld': long_int, '%llu': long_int,
             '%f': float, '%lf': float,
             '%g': float, '%lg': float,
             '%s': str, '%p': int,
             '%n': int, '%x': int, '%X': int}

# Configure the mapping from RT to the names used in the target
# language, e.g. set 'int' to 'INTEGER' if in ansi mode, '%d'
# to '%ld' etc.
NAMES = {}

# N.B. To map from Python types to a different function, type the
# desired name into the TEMPLATES map above.


