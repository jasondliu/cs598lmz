import types
# Test types.FunctionType
print types.FunctionType

# Test types.BuiltinFunctionType
print types.BuiltinFunctionType

# Test types.NativeType
print types.NativeType

# Test types.BuiltinType
print types.BuiltinType

# Test types.BuiltinMethodType
print types.BuiltinMethodType

# Test types.GroundType
print types.GroundType


"""
Test Suite used to verify PyObjectType.
"""

print '\n-- Test object types --\n'

print 'Testing types module.'
print types.ObjectType
print types.InstanceType
print types.TypeType


print '\n-- Test Types.py Methods --\n'

print 'Testing getType().'
testObject = TestObject()
print getType( testObject )


print '\nTesting getTypeDictionary().'
# Test getTypeDictionary()
print getTypeDictionary()


print '\nTesting iterObjectsOfType().'
# Test iterObjectMethods()
for o in iterObjectsOfType( TestObject ):
    print o

print '\nTesting get
