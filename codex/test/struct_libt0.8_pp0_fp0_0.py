import _struct
import _io

# http://stackoverflow.com/questions/20434466/python-speed-test-with-mock

import timeit
import functools

def stmt(stmts, globals):
    try:
        exec(stmts, globals)
    except Exception as e:
        return e

def time_usage(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        start_time = timeit.default_timer()
        result = f(*args, **kwargs)
        end_time = timeit.default_timer()
        print("{0} took {1}s".format(f.__name__, end_time - start_time))
        return result
    return wrapped

def timeit_test(stmt, globals):
    #print(stmt)
    f = functools.partial(stmt, globals=globals)
    globals['time_usage'] = time_usage
