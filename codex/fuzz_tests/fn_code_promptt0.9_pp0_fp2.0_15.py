fn = lambda: None
# Test fn.__code__, fn.__defaults__ and fn.__closure__
for fnattr in dir(fn):
    try:
        getattr(fn, fnattr)
        print(fnattr)
    except AttributeError as e:
        pass
