import io
# Test io.RawIOBase
class MyIO(io.RawIOBase):
    def readinto(self, b=bytearray()):
        return 0
    
# redirect io.RawIOBase.readinto to an array (get arg position checking)
import array
redirected = io.RawIOBase.readinto
# redefine readinto (no inspect.signature due to conditional logic)
def myreadinto(self, b):
    return redirected(self, array.array('B', b))
# replace method in io.RawIOBase parent
io.RawIOBase.readinto = myreadinto

import sys, StringIO
buf = StringIO.StringIO()
# test
sys.stdout = buf
try:
    MyIO().readinto('') # uses bytearray()
finally:
    sys.stdout = sys.__stdout__
buf.getvalue()
</code>
yields
<code>*** TypeError: 'str' does not support the buffer interface
</code>
While the above may be clumsy and work-around based, it does illustrate the problem, I think.
