fn = lambda: None
# Test fn.__code__ works:
fn.__code__
fn()

# Test fn.__code__.co_varnames works:
fn.__code__.co_varnames
fn.__code__.co_varnames[0]
fn.__code__.co_varnames[1]


class Meta(type):
    def __repr__(self):
        return self.__name__

class C(metaclass=Meta):
    def __init__(self):
        self.x = 1

c = C()
c.x

class Meta(type):
    def __repr__(self):
        return self.__name__

class A(metaclass=Meta):
    def __init__(self):
        self.x = 1

class B(A, metaclass=Meta):
    def __init__(self):
        self.y = 2
        super().__init__()

b = B()
b.x
b.y


fn = lambda x: x

# Test fn.__annotations__ works:
