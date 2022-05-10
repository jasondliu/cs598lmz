import types
# Test types.FunctionType
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type(x for x in range(10)) == types.GeneratorType)
# Test types.LambdaType
f = lambda x: x
print(f(10))
# Test types.GeneratorType
print(isinstance((x for x in range(10)), types.GeneratorType))
print(isinstance([], types.GeneratorType))
print(isinstance({}, types.GeneratorType))
print(isinstance('abc', types.GeneratorType))

# Test types.UnboundMethodType
class People(object):
    def say(self):
        print('hello world')
p = People()
print(p.say())
print(type(p.say))
print(type(People.say) == types.UnboundMethodType)

# Test types.MethodType
class People(object):
    def say(self):
        print('hello world')
p = People()
print(p.say())
print(
