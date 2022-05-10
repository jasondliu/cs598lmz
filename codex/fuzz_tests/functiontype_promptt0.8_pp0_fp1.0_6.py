import types
# Test types.FunctionType
#
def f(): pass
for x in range(len(dir(types))):
    name = dir(types)[x]
    if name[:11] == 'FunctionType':
        attr = getattr(types, name)
        if type(attr) == types.FunctionType:
            print '%s is FunctionType' % name
#
# Now we have to figure out where FunctionType is:
#
print types.FunctionType is str.__class__
print types.FunctionType is tuple.__class__
print types.FunctionType is types.FunctionType
print types.FunctionType is types.InstanceType
print types.FunctionType is types.MethodType
print types.FunctionType is types.UnboundMethodType
#
# Aha.  So what is types.FunctionType?
#
print types.FunctionType
print type(types.FunctionType)
#
# It doesn't look like a function.  So what is it?
#
print types.FunctionType.__class__
print types.FunctionType.__class__.__class__
print type(types.FunctionType.__class
