from _struct import Struct
s = Struct.__new__(Struct)
s.pack = lambda format, *args, **kwargs: _struct.pack(format, *args, **kwargs)
s.unpack = lambda string, *args, **kwargs: _struct.unpack(string, *args, **kwargs)
s.calcsize = lambda format, *args, **kwargs: _struct.calcsize(format, *args, **kwargs)
struct = s


def ordereddict():
    return OrderedDict({})

@contextmanager
def pushd(path):
    curdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(curdir)

def thread(*args, **kwargs):
    def f(*a, **k):
        with pushd(args[0]):
            args[0] = os.getcwd()
            return args[1](*args, **kwargs)
    return threading.Thread(target=f, args=a, kwargs=k)
