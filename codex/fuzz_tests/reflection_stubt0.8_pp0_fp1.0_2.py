fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


class ReferenceTest:

    """Class with different types of references in its code object."""

    def __init__(self, arg):
        self.arg = arg
        self.attr = arg

    def func(self, arg):
        return self.attr, arg

    def func_closure(self, arg):
        x = [1]
        def inner(arg):
            return self.attr, arg, x
        return inner

    def func_eval(self, arg):
        code = compile("(self.attr, arg)", "<string>", "eval")
        return eval(code)

    def func_exec(self, arg):
        global some_fn
        code = compile("some_fn = self.attr", "<string>", "exec")
        exec(code, globals())
        return some_fn

    def func_exec_finally_return(self, arg):
        try:
            x = 1
        finally:
            x = 2
        return x

    def func_exec_finally_result(self, arg):
       
