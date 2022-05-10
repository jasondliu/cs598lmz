import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

print(bytes(view))

# view.objc_class.__str__ = lambda self: "mystr"

import gc
gc.collect()
print(gc.garbage)
"""

# debug
# assert False
# preamble = 'import objc; objc.options.set_debug(75)'

r = test.run(preamble, script)
r.assert_('b"a"')
r.assert_(None in gc.garbage)
if True:
    assert None in gc.garbage
    # This should raise an exception because it would trigger the dealloc
    # of the object that is currently being tracked down.
    r.unload_cffi_module()
    r.assert_('Leaked objc_object at')
    assert len(gc.garbage) == 1
