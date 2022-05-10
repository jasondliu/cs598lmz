gi = (i for i in ())
# Test gi.gi_code.co_flags

def f():
    yield 1

def f_no_yield():
    pass

def f_with_yield():
    yield 1

def f_with_yield_in_try():
    try:
        yield 1
    except:
        pass

def f_with_yield_in_try_finally():
    try:
        yield 1
    finally:
        pass

def f_with_yield_in_try_finally_yield():
    try:
        yield 1
    finally:
        yield 2

def f_with_yield_in_try_finally_yield_except():
    try:
        yield 1
    finally:
        yield 2
    except:
        pass

def f_with_yield_in_try_finally_yield_except_else():
    try:
        yield 1
    finally:
        yield 2
    except:
        pass
    else:
        yield 3

def f_with_yield_in_try_finally_y
