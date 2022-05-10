import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n):
        return self.f.read(n)
    def close(self):
        return self.f.close()
file = File(open('test.txt', 'rb'))
"""

"""
# 可以使用类的方法来接收一个类的对象，并且返回一个类的对象
class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return '<A (%d, %d)>' % (self.x, self.y)
    @classmethod
    def from_xy(cls, x, y):
        return cls(x, y)
    @classmethod
    def from_tuples(cls, tuples):
        return cls(*tuples)

