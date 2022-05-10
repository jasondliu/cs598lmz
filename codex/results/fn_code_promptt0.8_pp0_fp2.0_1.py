fn = lambda: None
# Test fn.__code__ is a structure, not a real function
fn.__code__ = struct.pack(
    'iiiiiiii',
    0x02000000, # magic, for functionality of the subprocess module
    0, # arg count
    0, # nlocals
    0, # stacksize
    0, # flags
    1, #codesize
    0, #nconstants
    0, #names
    0, #varnames
    0, #filename
    0, #name
    0, #firstlineno
    1, #lnotab
)
# Test fn.__code__.co_code is an arbitrary string, not a real code object
fn.__code__.co_code = b'a' * 0x10000
print('PID: %i' % os.getpid())
# Crash
fn()
