from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)[:1]

# now, this is the actual code
# but I think it's much less elegant than my original solution

import inspect
def get_var_name(var):
    for fi in reversed(inspect.stack()):
        names = [var_name for var_name, var_val in fi.frame.f_locals.items() if var_val is var]
        if len(names) > 0:
            return names[0]
    return None

# and a final version which doesn't rely on inspect
# and is based on a comment by user "Unutbu"
# https://stackoverflow.com/a/1843789/49386

import sys

def get_var_name(var, frame=0):
    frameinfo = sys._getframe(frame+1)
    for name in frameinfo.f_code.co_varnames:
        if frameinfo.f_locals[name] is var:
            return name
    return None

# and here's a version
