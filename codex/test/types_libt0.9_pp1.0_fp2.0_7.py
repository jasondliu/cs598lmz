import types
types.MethodType(func, None, type)

types.MethodType(func, None, type(None))

types.MethodType(func, None, type(object))

# __new__ return wrong type (Object21FromArgs)
tester = Object21_args()

# __new__ return wrong type (Object22FromArgs)
tester = Object22_args()

# __new__ return wrong type (Object23FromArgs)
