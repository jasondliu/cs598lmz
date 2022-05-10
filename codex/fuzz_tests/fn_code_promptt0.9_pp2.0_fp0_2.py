fn = lambda: None
# Test fn.__code__.co_argcount
ret_type = int

def make_fn(*args):
    if len(args) == 0:
        return testfn
    elif len(args) == 1:
        return testfn
    elif len(args) == 2:
        return testfn
    elif len(args) == 4:
        return testfn

# Test fn(*args)
def call_with_no_args():
    return make_fn()()

def call_with_one_arg():
    return make_fn(1)()

def call_with_two_args():
    return make_fn(1,2)()

def call_with_four_args():
    return make_fn(1,2,3,4)()

# Test inspect.stack()
def test_stack():
    retval = inspect.stack()

def yield_frame(i):
    try:
    # The following line causes the "yield" traceback
    #   which this function will catch.
        yield i
    except:
        i += 1
       
