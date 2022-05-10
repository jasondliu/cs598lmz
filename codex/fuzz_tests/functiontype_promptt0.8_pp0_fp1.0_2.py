import types
# Test types.FunctionType
# Should print "This is a function"
print types.FunctionType(types.FuncType(types.CodeType(
     0, 1, 1, 0, 'd\x00\x00S', ('', '', None, None),
     (), (), ('',), '', '', 0, '', None, None), {}),{})('',)

# Test types.ClassType
# Should print "This is a class"
print types.ClassType('TestType', (object,), 
    {'__init__': types.MethodType(types.FuncType(types.CodeType(
     0, 0, 0, 0, 'd\x00\x00S', ('', '', None, None),
     (), (), ('',), '', '', 0, '', None, None), {}, None, None),
     types.ClassType('TestType', (object,), {}), types.ClassType('TestType',
     (object,), {}))})().__init__()

# Test types.InstanceType
# Should print "This is an instance"
print types.Instance
