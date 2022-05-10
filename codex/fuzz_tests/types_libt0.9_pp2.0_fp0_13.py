import types
types.MethodType(my_decorator, None)
def my_decorator(my_func):
    def wrapper(*args, **kwargs): # 1
        print 'Calling decorated function...'
        return my_func(*args, **kwargs) # 2
    return wrapper
def my_new_decorator(my_func):
    def wrapper(*args, **kwargs): # 1
        print 'Calling decorated function...'
        return my_func(*args, **kwargs) # 2
    return wrapper
my_new_decorator(my_func)
@my_decorator
def my_func():
    print 'my_func() called.'
my_func()

import time 
def performance(unit): 
    def per_decorator(f): 
        def fn(*args, **kwargs): 
            t1 = time.time()
            r = f(*args, **kwargs)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
           
