fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = gi.gi_frame.f_code
gi.gi_frame.f_locals = gi.gi_frame.f_globals
fn.__name__ = 'gen'
gi.gi_name = gi.__name__ = 'gen'
print(gi.gi_code.co_name, fn.__code__.co_name)

import sys
print('REPL', sys.flags.interactive, sys._run_code is None)
print()

# __closure__ for top-level-functions is None
print('__closure__ for top-level-functions:', fn.__closure__ is None)

# co_freevars is empty
print('co_freevars:', fn.__code__.co_freevars, '\n')


# builtin functions
def one_arg(arg):
    return arg + 1

def two_arg(arg1, arg2):
    return arg1 + arg2

def no_arg():
    return None

print(one_arg, two_
