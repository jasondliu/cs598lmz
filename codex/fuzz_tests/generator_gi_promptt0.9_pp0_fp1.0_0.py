gi = (i for i in ())
# Test gi.gi_code.co_flags

# Verify the test itself
try:
    next(gi)
except TypeError:
    try:
        next(gi)
    except RuntimeError:
        try:
            next(gi)
        except StopIteration:
            pass
        except RuntimeError:
            raise Exception("Why am I still running?")
    else:
        raise Exception("Expected next(gi) to raise RuntimeError")
else:
    raise Exception("Expected next(gi) to raise TypeError")
else:
    pass


def f():
    pass
# Check that disassembling a function with no code raises a ValueError
try:
    dis.dis(f)
except ValueError:
    pass
else:
    raise Exception("Expected disassembling f() to raise a ValueError")


def f():
    pass
f.__code__ = 5
# Check that disassembling a function with a bad code object raises a TypeError
try:
    dis.dis(f)
except TypeError:
    pass
else:
    raise Exception("Expected disassembling f
