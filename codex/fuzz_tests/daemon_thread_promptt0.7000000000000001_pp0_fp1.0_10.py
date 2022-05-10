import threading
# Test threading daemon flag.
threading.Thread(target=lambda: 1, daemon=True).start()
# Test isinstance comparison with classes, not types.
assert isinstance(threading.Thread(), threading.Thread)
# Test passing a callable and args.
def foo():
    return 1
t = threading.Thread(target=foo, args=(1, 2, 3))
t.start()
# Tests passing a callable and kwargs.
def foo(**kwargs):
    return 1
t = threading.Thread(target=foo, kwargs={'a': 1, 'b': 2})
t.start()
# Tests passing args and kwargs.
def foo(*args, **kwargs):
    return 1
t = threading.Thread(target=foo, args=(1, 2, 3), kwargs={'a': 1, 'b': 2})
t.start()
# Test that a thread can be started more than once.
def foo():
    pass
t = threading.Thread(target=foo)
t.start()
# Test that a thread can be started more than
