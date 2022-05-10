import weakref
# Test weakref.ref()

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print "Foo.__del__(%s)" % self.name

def bar(obj):
    print "bar(%s)" % obj.name

f = Foo("f")
r = weakref.ref(f, bar)
print "created weakref %r" % r
print "calling bar()"
bar(f)
print "deleting f"
del f
print "calling bar()"
bar(r())
print "calling bar() again"
bar(r())
print "done"
