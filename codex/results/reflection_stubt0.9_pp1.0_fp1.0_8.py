fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

try:
    fn()
except ValueError:
    print('ValueError')

'''Note: The error is thrown in ceval.c, where the opcode POP_BLOCK has to
be interpreted. This implies that a yield statement in the invoked function
is being popped, but the interpreter is out of generators. V. tried to
figure out exactly what's happening, but without success.
Note also that this is a cross-interpreter bug. V. phoned here and U. can
confirm.'''

# The error message says that "generator already executing", when in fact
# this is a function (which can be called any number of times). The error
# message should say something more like "calling nested generator".
