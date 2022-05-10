fn = lambda: None
# Test fn.__code__.co_varnames
fn.__code__.co_varnames
# Test fn.__code__.co_flags
fn.__code__.co_flags
# Test fn.__code__.co_filename
fn.__code__.co_filename

# Test fn.__closure__
fn.__closure__


def fn(arg1):
    def inner():
        return arg1
    return inner

fn('a')()
fn('b')()


def fn(arg1):
    def inner():
        return x
    x = arg1
    return inner

fn('a')()
fn('b')()


def fn(arg1):
    def inner():
        return x
    x = arg1
    return inner

fn('a')()
fn('b')()
