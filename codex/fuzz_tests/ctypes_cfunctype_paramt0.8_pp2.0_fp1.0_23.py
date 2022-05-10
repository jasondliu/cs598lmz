import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)

class TestFunction(object):
    def __init__(self, func, args, kwargs, res=None):
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.res = res

    def __call__(self):
        return self.func(*self.args, **self.kwargs)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class TestPipe(object):
    def __init__(self, test_function, worker):
        self.test_function = test_function
        self.worker = worker

    def __bool__(self):
        return self.test_function(*self.worker.args, **self.worker.kwargs)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.test
