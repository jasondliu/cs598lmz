fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()


def fn():
    return
    yield


print(fn())


def fn():
    return 1
    yield


print(fn())


def fn():
    if True:
        return
        yield
    else:
        return 1
        yield


print(fn())


def gen():
    return
    yield


def fn():
    return gen()


print(fn())


def fn():
    yield


fn().throw()


def fn():
    if True:
        yield
    else:
        return


fn().throw()


def fn():
    yield
    return 1


print(fn().throw())


def fn():
    if True:
        yield
    else:
        return 1


print(fn().throw())


def gen():
    return 1
    yield 1


def gen2():
    yield from gen()
    yield 2


print(list(gen2()))


def gen():
    yield from range(5)
    return


def gen2():
    yield from ((
