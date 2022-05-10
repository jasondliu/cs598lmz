fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
g_ = (lambda: 1)()
fn.__code__.co_names.__iter__ = g_
gi.gi_running = fn
fn.__code__.co_varnames = (gi,)
fn.__code__.co_names = (gi,)

def ggg():
    print("hi")
    for i in range(3):
        ggg._nametranslate_ = ()
        ggg.__name__ = chr(i+97)
        print(ggg.__name__)
    return ggg.__name__

ggg()
