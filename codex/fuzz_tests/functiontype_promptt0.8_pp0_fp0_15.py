import types
# Test types.FunctionType and types.MethodType
class test(object):
    def __init__(self):
        print "ok"
    def test(self):
        print "foo"

test()
test.__init__
test.__init__.im_func
test.__init__.im_class
test.__init__.im_self
test.test.im_class
test().test

# Test types.DictionaryType
test.__dict__
test.__dict__.keys()
test.__dict__.values()
test.__dict__["test"]

# Test types.LambdaType
a = lambda x:x+1
print a(1)

# Test types.GeneratorType
b = (x+1 for x in range(5))
print type(b)
for x in b:
    print x,
print

# Test types.ClassType
class Foo:pass
print type(Foo)

# Test types.InstanceType
class Bar:pass
bar = Bar()
print type(bar)

# Test types.MethodType
class Test
