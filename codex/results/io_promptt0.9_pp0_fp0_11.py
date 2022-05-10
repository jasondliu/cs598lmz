import io
# Test io.RawIOBase.getstate
import pickle

try:com
    import io
    import pickle
# io.RawIOBase.__getstate__ removed in Python 3.3
except AttributeError:
    import sys
    print("SKIP")
    sys.exit()

class MyIO(io.RawIOBase):
    def readinto(self, buf):
        pass

x = MyIO()
print(pickle.loads(pickle.dumps(x)).__class__)

x = MyIO()
y = pickle.loads(pickle.dumps(x, -1))
print(y.__class__, y.encoding)

x = MyIO()
y = pickle.loads(pickle.dum
