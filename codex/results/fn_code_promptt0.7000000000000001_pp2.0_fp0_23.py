fn = lambda: None
# Test fn.__code__.__class__.co_flags & 0x20
# Python 3.4 on Windows fails
g = globals()
for f in dir(fn.__code__):
    try:
        g[f] = getattr(fn.__code__, f)
    except TypeError: pass
# End support code

# Copied from http://bugs.python.org/issue5154

class NoInlineAssignments(Exception): pass

class MalformedBytecode(Exception): pass

def _check_bytecode(co):
    code = co.co_code
    names = co.co_names
    consts = co.co_consts
    n = len(code)
    i = 0
    extended_arg = 0
    while i < n:
        op = code[i]
        if op >= HAVE_ARGUMENT:
            op_name = opname[op]
            if op_name.startswith('UNARY_'):
                op_name = op_name[len('UNARY_'):]
            if op_name.startsw
