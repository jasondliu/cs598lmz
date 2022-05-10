fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__qualname__ = 'fn'
fn.__module__ = 'test_code_object'
fn.__annotations__ = {}
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__kwdefaults__ = None
fn.__closure__ = ()
fn.__globals__ = {}
fn.__doc__ = None

# This is a function object with a single bytecode instruction.
fn_single_instruction = (lambda: None).__code__.co_consts[0]

# This is a function object with a single bytecode instruction,
# but the bytecode instruction is a jump.
fn_single_jump = (lambda: None).__code__.co_consts[1]

# This is a function object with a single bytecode instruction,
# but the bytecode instruction is an extended jump.
fn_single_extended_jump = (lambda: None).__code__.co_consts[2]

# This is a function object with a single
