import types
# Test types.FunctionType in namespace
def gettype(b):
    if isinstance(b, types.FunctionType):
        return b()
    return b

def testtype():
    return gettype(42)

def testtype2():
    return gettype(testtype)

#print testtype()
#print testtype2()
assert testtype() == 42
assert testtype2() == 42

# Test types.FunctionType in class
class C(object):
    def __init__(self):
        self.x = 42
    def gettype(self, b):
        if isinstance(b, types.FunctionType):
            return b()
        return b
    def testtype(self):
        return self.gettype(self.x)
    def testtype2(self):
        return self.gettype(self.testtype)

c = C()
#print c.testtype()
#print c.testtype2()
assert c.testtype() == 42
assert c.testtype2() == 42

# Test types.FunctionType in nested class
class C(object):
