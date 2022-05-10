fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'code' object is not iterable

# 使用类的__call__方法来实现callable对象

class Callable(object):
    def __init__(self, anycallable):
        self.__call__ = anycallable

def show():
    print('show...')

c = Callable(show)

print(callable(c))

c()

# True
# show...
