fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
values = fn.__code__.co_varnames[:fn.__code__.co_argcount]

def purge(*names):
    """Remove the specified names from some Python variables.

    Variables spent are all lowercase and uppercase, and
    builtins.

    Accepts a list or tuple of names or a string."""
    if isinstance(names, basestring):
        names = names.split()
    for n in names:
        if n in values:
            del values[n]
        nn = n.upper()
        if nn in values:
            del values[nn]

if __name__ == '__main__':
    import sys
