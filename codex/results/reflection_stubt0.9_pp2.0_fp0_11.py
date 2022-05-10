fn = lambda: None
gi = (i for i in ())
fn.__code__ = ()
for func in (type, getattr, dir, gi.throw, gi.close, gi.send, gi.__anext__,
             gi.__aiter__, assign, and, or, in_, is, is_not, id, del_, name,
             lambda: (), max, min, abs, float, int, str, ord, chr, hash,
             complex, type, divmod, div, mod, pow, fn.__code__.co_filename,
             fn.__code__.co_name):
    try:
        try:
            func()
        except TypeError:
            r, c = os.path.splitext(func.__code__.co_filename)
            if func.__code__.co_name == '<lambda>':
                c = '<lambda>'
            if not os.path.exists(func.__code__.co_filename):
                print('Error: not found ' + func.__code__.co_filename)
            tests.append((r, c))
    except AttributeError
