from types import FunctionType
list(FunctionType(lambda x:x+x, globals(), 'f').__code__.co_varnames)

class Function():
    def __init__(self, fn):
        self.fn = fn

    def get_vars(self):
        return list(self.fn.__code__.co_varnames)

def get_vars(fn):
    return list(Function(fn).get_vars())
</code>
I am wondering if there is a better way to do this? Also, I am wondering if I could get the line number of each variable in the function?

