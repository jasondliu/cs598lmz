import codecs
# Test codecs.register_error, but need a UnicodeDecodeError
b'\xe9'.decode('ascii')

# Test @wraps
@logged
def f(): pass

def f2(): pass

f2 = logged(f2)

# Test @overload
@overload
def f(x:int) -> int: return x + 2
def g(): 
    a = f(2)

# Test abc.abstractmethod
class C(object, metaclass=ABCMeta):
    @abstractmethod
    def f(self): pass
