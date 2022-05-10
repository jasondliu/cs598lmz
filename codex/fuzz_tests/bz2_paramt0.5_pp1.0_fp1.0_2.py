from bz2 import BZ2Decompressor
BZ2Decompressor().decompress("foo")

# __all__ can be set in the module body
__all__ = ["BZ2Decompressor"]

# __all__ can be set in a class body
class BZ2Decompressor(object):
    __all__ = ["decompress"]
    def decompress(self, data):
        pass

# __all__ can be set in a function body
def decompress(data):
    __all__ = ["decompress"]
    pass

# __all__ can be set in a try body
try:
    __all__ = ["decompress"]
except:
    pass

# __all__ can be set in an except body
try:
    pass
except:
    __all__ = ["decompress"]

# __all__ can be set in a finally body
try:
    pass
finally:
    __all__ = ["decompress"]

# __all__ can be set in an if body
if True:
    __all__ = ["decompress"]

# __all__ can be set in an elif
