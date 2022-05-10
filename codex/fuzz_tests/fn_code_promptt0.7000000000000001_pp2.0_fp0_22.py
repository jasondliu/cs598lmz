fn = lambda: None
# Test fn.__code__
try:
    fn.__code__
except AttributeError:
    print("SKIP")
    raise SystemExit

# Test fn.__code__.co_freevars
try:
    fn.__code__.co_freevars
except AttributeError:
    print("SKIP")
    raise SystemExit

def fn():
    x = 1
    y = 2
    z = 3
    def nested():
        return x + y + z
    return nested

fn = fn()
# Test fn.__code__.co_freevars
print(fn.__code__.co_freevars)
print(fn.__closure__)
