from types import FunctionType
a = (x for x in [1])

print(type(a))
# <class 'generator'>


# wrapper
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log
def now():
    print("2016-06-19")

@log2("execute")
def now2():
    print("2016-06-19")

now()
now2()


# executor

def exe(func, *args, **kwargs):
    return func(*args, **kwargs)

print(exe(int, "10"))
print(exe(str, 10))
