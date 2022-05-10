fn = lambda: None
# Test fn.__code__.co_filename
co_fn.__code__.co_filename = "test.py"
assert co_fn.__code__.co_filename == "test.py"

# Test fn.__closure__
def f():
    a = 5
    def g():
        return a
    return g

c = f()
assert c.__closure__[0].cell_contents == 5

# Test fn.__code__.co_lnotab
def f():
    a = 5
    b = 6

assert f.__code__.co_lnotab == b"\x00\x01\x0c\x01"

# Test fn.__code__.co_zombieframe
try:
    raise ZeroDivisionError
except Exception as e:
    assert e.__traceback__.tb_frame.f_code.co_zombieframe is not None

# Test fn.__code__.co_filename
assert fn.__code__.co_filename == __file__

# Test fn.__code__.co_first
