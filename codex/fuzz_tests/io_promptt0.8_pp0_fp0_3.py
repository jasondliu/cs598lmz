import io
# Test io.RawIOBase
r = io.RawIOBase.read
w = io.RawIOBase.write
c = io.RawIOBase.close
f = io.RawIOBase.flush
try:
    t = io.RawIOBase.truncate
except AttributeError: pass
else: assert 0
f.im_self
c.im_self
r.im_self
w.im_self
f.im_class
c.im_class
r.im_class
w.im_class
r.im_func
c.im_func
r.im_func
w.im_func
r.im_self is None
w.im_self is None
c.im_self is None
f.im_self is None
r.im_class is io.RawIOBase
w.im_class is io.RawIOBase
c.im_class is io.RawIOBase
f.im_class is io.RawIOBase
r.im_func is io.RawIOBase.read
w.im_func is io.RawIOBase.write
c.im_func is
