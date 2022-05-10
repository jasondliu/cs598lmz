import types
# Test types.FunctionType - no input is accepted, by the moment
types.FunctionType(body = 'x=1',globals=globals(),argdefs=())

# Test types.LambdaType - no input is accepted, by the moment
types.LambdaType(body = 'x=1',globals=globals(),argdefs=())
 
# Can not test types.ClassType and types.TypeType, because as far as I know
# there is no syntax for it in Python. I list these because 2.0 test
# shows them.

# Testing types.FileType - no input, by the moment
types.FileType(args='')

# Testing types.XRangeType - no input, by the moment
types.XRangeType(arg=0, **dict(stop=100))

# Testing types.MemberType - no input, by the moment
types.MemberType(name = 'x',globals=globals())

# I think this test is o.k. although I don't unserstand what is a module
# and how to create one
l =
