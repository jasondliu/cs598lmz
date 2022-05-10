import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

class My(metaclass=Meta):
    def __init__(self, func):
        self.func = func
    def hello(self):
        return self.func()

My = type("My", (object,), {"__init__": fun, "hello": fun})

if __name__ == "__main__":
    m = My()
    print(m.hello())
</code>
My problem is that I would like to be able to use a function that uses <code>self</code> as the first argument. 
For example:
<code>@FUNTYPE
def fun(self, arg):
    return "hello " + self.attribute + arg
</code>
Unfortunately, the above code doesn't work since <code>self</code> is not defined.
I know I can do something like:
<code>@FUNTYPE
def fun(arg):
    return "hello " + self.attribute + arg
</code>
But that would mean that I would have to execute <code>fun(m, arg)</code> instead of <code>m.
