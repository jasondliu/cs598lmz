fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_frame)()

code_info(gi)
code_info(fn)
code_info(gi.gi_code)

gi_code = type(gi.gi_frame)

def run_code(codeobj, *args, **kwargs):
    """
    Create a new frame, run a code object, and return the result
    """
    # Create a new frame
    frame = gi_code()
    frame.f_code = codeobj
    # f_locals is a dict, but it doesn't do anything
    frame.f_locals = kwargs
    # Pass in any args, but they don't do anything either
    frame.f_globals = args
    # Evaluate the code object. We need to fetch the builtin "locals"
    frame.f_builtins = globals()["__builtins__"]
    frame.f_builtins["locals"] = lambda: locals()
    # Execute the code!
    return frame.f_code.__call__(frame)

