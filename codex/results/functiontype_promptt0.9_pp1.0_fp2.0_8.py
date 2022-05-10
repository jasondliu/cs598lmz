import types
# Test types.FunctionType
class f:
    def g(self): pass
test_values = [abs, (lambda x: x)], [f.g, f().g], [f.g, (lambda self:None)]

class BadType(object): pass

for v in test_values:
    func1 = v[0]
    func2 = v[1]
    func3 = BadType()
    func4 = BadType()

    if not isinstance(func1, types.FunctionType):
        print "abs is not a types.FunctionType"

    if not isinstance(func2, types.FunctionType):
        print "lambda x: x is not a types.FunctionType"

    if isinstance(func3, types.FunctionType):
        print "BadType() is a types.FunctionType"

    if isinstance(func4, types.FunctionType):
        print "(lambda: None) is a types.FunctionType"

# Test types.LambdaType
class f:
    def g(self): pass

x = (lambda x: x)
y = f.g
z
