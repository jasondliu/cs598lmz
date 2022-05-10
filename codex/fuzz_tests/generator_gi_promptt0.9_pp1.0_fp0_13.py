gi = (i for i in ())
# Test gi.gi_code is not set.
XCTAssertAttributeError(gi, 'gi_code')

class class_with_gi1:
    def __iter__(self): self.gi = (i for i in ())

gi = class_with_gi1().gi
# Test gi.gi_code is not set.
XCTAssertAttributeError(gi, 'gi_code')

def func_with_gi1():
    gi = (i for i in ())

gi = func_with_gi1()
# Test gi.gi_code is not set.
XCTAssertAttributeError(gi, 'gi_code')

# Gi with both generator & code objects
# Gi.gi_frame contains set of hidden attributes.

class class_with_gi2:
    def __init__(self):
        self.gi = (i for i in ())
        self.code = type(self.gi).__iter__.__code__
    def __iter__(self):
        self.frame = sys._getframe(0)

gi = class_with_gi2().gi
