from types import FunctionType
a = (x for x in [1])
a = list(a)
print(type(a[0]))
class a(object):
    def __init__(self, *args, **kwargs):
        super(a, self).__init__()
    test = lambda: 42
    def c(self):
        assert self.test() == 42
        pass
a().c()
