import weakref
# Test weakref.ref() and weakref.proxy()

# Create a class with a __del__ method
class C:
    def __init__(self, n):
        self.n = n
    def __del__(self):
        print "C.__del__", self.n

# Create a class with a __cmp__ method
class D:
    def __init__(self, n):
        self.n = n
    def __cmp__(self, other):
        return cmp(self.n, other.n)

# Create a class with a __call__ method
class E:
    def __init__(self, n):
        self.n = n
    def __call__(self):
        return self.n

# Create a class with a __getitem__ method
class F:
    def __init__(self, n):
        self.n = n
    def __getitem__(self, i):
        return self.n + i

# Create a class with a __getattr__ method
class G:
    def __init__(self, n):

