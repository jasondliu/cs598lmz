from types import FunctionType
list(FunctionType(defer, globals(), name=func.__name__, argdefs=func.func_defaults, closure=c))

# yield does not work for generator/defer
def defer_closure(func, *args, **kw):
    def wrapper():
        yield func(*args, **kw)
    return wrapper

def defer(func):
    @wraps(func)
    def wrapper(*args, **kw):
        return defer_closure(func, *args, **kw)
    return wrapper


@defer
def getimage(url, filename="out.jpg"):
    import subprocess
    subprocess.call("wget -O {0} {1}".format(filename, url), shell=True)
    yield

task = getimage("http://www.ask.com/profile/ACF3A7136DC82D9799CECBBA8672AE9F")
# print task.next()
run_with_reactor(task)

@defer
def image2str(filename, strname="out.txt"):
    import subprocess

