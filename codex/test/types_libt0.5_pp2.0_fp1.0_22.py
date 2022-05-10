import types
types.MethodType(lambda n: n, None, None)

# rpython.rlib.objectmodel.freeze_
def freeze_(n):
    return n

class A(object):
    def __init__(self, n):
        self.n = n

    def __add__(self, m):
        return A(self.n + m)

    def __sub__(self, m):
        return A(self.n - m)

    def __mul__(self, m):
        return A(self.n * m)

    def __floordiv__(self, m):
        return A(self.n // m)

    def __mod__(self, m):
        return A(self.n % m)

    def __divmod__(self, m):
        return A(self.n // m), A(self.n % m)

    def __pow__(self, m):
        return A(self.n ** m)

    def __lshift__(self, m):
        return A(self.n << m)

