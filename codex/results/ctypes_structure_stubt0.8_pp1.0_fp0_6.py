import ctypes

class S(ctypes.Structure):
    x = None

def test():
    print S.x
    print S.x, 'hello'
    print "%s" % S.x
    print "%s world" % S.x

test()
</code>
output:
<code>c_void_p(None)
c_void_p(None) hello
None
None world
</code>

