from types import FunctionType
list(FunctionType(function_with_any_tree_instance, globals(), "function_with_any_tree_instance")(cute_function))

def foo(f):
    return f(3)
env = Environment(foo)
lst = list(FunctionType(foo, globals(), "foo")(add_one))
assert lst == [7]


def curried_plus(x):
    def plus_x(y):
        return y + x
    return plus_x

class Environment(dict):
    def __init__(self, parent=None):
        self.parent = parent
    def __getitem__(self, item):
        if item in self:
            return super(Environment, self).__getitem__()
        if self.parent is not None:
            return self.parent.__getitem__(item)
        raise KeyError(item)

def run_cute(original_func, *args):
    def _run(cute_func):
        env = Environment()
        env.update(cute_func.code.func_globals)
