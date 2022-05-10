from types import FunctionType
list(FunctionType(f.func_code,f.func_globals))

"""


"""
# -*- coding: utf-8 -*-
import functools

def log(func):
    def wrapper(*args, **kw):
        print "function name is: %s" % func.__name__
        return func(*args, **kw)
    return wrapper

@log
def now():
    print "2017-07-11"

now()

"""


"""
# -*- coding: utf-8 -*-
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print "%s occurs at %s" % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print "2017-07-11"

now()
"""


"""
# -*- coding: utf-8 -*-
import functools

def log(func):
    @functools.
