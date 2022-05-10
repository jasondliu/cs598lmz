import types
types.MethodType(func, None, type)

types.MethodType(func, None, type(None))

types.MethodType(func, None, type(object))

# __new__ return wrong type (Object21FromArgs)
tester = Object21_args()

# __new__ return wrong type (Object22FromArgs)
tester = Object22_args()

# __new__ return wrong type (Object23FromArgs)
tester = Object23_args()

# __new__ return wrong type (Object24FromArgs)
tester = Object24_args()

# __new__ return wrong type (Object25FromArgs)
tester = Object25_args()

types.MethodType(func, None, foo.Bar)

types.MethodType(func, None, foo.Bar())

types.MethodType(func, None, foo.Bar(1))

"""
class NewArgs(object):
    def __new__(cls, x, y):
        self = super(NewArgs, cls).__new__(cls)
        self.x =
