fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
 
for j in (0, 1):
    fn.__code__.co_argcount = gi.gi_code.co_argcount = j
    try:
        next(gi)
    except:
        pass
    else:
        print("TypeError not raised")

for j in (-1, 2**9):
    fn.__code__.co_argcount = gi.gi_code.co_argcount = j
    try:
        next(gi)
    except ValueError:
        pass
    else:
        print("ValueError not raised")

for j in (-1, 2**9):
    fn.__code__.co_argcount = gi.gi_code.co_argcount = ((yield from gi) for
            gi in ()).gi_code.co_argcount = j
    try:
        fn()
    except ValueError:
        pass
    else:
        print("ValueError not raised")

fn.__code__.co_
