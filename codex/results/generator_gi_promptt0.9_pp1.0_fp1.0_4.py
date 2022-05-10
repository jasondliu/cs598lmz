gi = (i for i in ())
# Test gi.gi_code returning native code object.
print(gi.gi_code.co_argcount)

# Test support of a few bytecode instructions
def f():
    print((yield))
    a = 0
    while a:
        a = yield a
    a = (yield a)
    print(a)
    return

g = f()
next(g)
if sys.version_info[:2] < (2, 6):
    if __debug__:
        g.send(4)
        with pytest.raises(ValueError):
            g.send(3.3)
        with pytest.raises(TypeError):
            g.send(object())
    else:
        # in optimized mode, we need a float object (not a float), otherwise
        # we get a TypeError at the "yield a"
        g.send(4)
        g.send(3.3)
        with pytest.raises(TypeError):
            g.send(object())
else:
    g.send(4)
    g.send(3.3
