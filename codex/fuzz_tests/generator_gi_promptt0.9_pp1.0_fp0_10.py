gi = (i for i in ())
# Test gi.gi_code with a mocked object that
# has all the attributes of a code object,
# except one.
code = type('code',(object,),{'foo':'bar'})()
gi.gi_code = code
assert gi.gi_code.foo == 'bar'
print gi
print '%r'%gi
#print '%r'%(gi,)


print 'args,'
fi = inspect.getargspec(f)
print fi
print fi.args
print fi.varargs
print fi.keywords
print fi.defaults
print 'tuple,',tuple.__code__.co_varnames[0]

print 'examine_builtins:'
print inspect.getargspec(tuple)
print inspect.getargspec(tuple.__init__)
print inspect.getargspec(tuple.__reversed__)

class FakeFunc(object):
    func_code = type('code',(object,),{'co_varnames':('spam','eggs'),'foo':'bar'})()
print inspect.get
