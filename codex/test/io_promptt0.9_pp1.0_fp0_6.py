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

