import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
x = 'hello'
x.__len__()

#%%
class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return 'MyList(%s)' % self.data
    def __add__(self, rhs):
        return MyList(self.data + rhs.data)
    def __mul__(self, rhs):
        return MyList(self.data * rhs)
    def __rmul__(self, lhs):
        return MyList(lhs * self.data)
    def __getitem__(self, index):
        return self.data[index]
    def __setitem__(self, index, value):
        self.data[index] = value
    def __delitem__(self, index):
        del self.data[index]
    def append(self, value):
        self.data.append(value)

