import weakref
# Test weakref.ref()
def test(func, *args):
    try:
        func(*args)
    except Exception:
        return 0
    else:
        return 1
def check(func, *args, **kwargs):
    failures = 0
    if not args:
        args = ({},)
    for a in args:
        if not test(func, a):
            failures += 1
    for a in kwargs:
        if not test(func, a):
            failures += 1
    return failures
def check_alive(func, *args, **kwargs):
    failures = 0
    if not args:
        args = ({},)
    for a in args:
        if test(func, a):
            failures += 1
    for a in kwargs:
        if test(func, a):
            failures += 1
    return failures
