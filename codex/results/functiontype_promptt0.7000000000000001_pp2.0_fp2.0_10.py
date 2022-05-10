import types
# Test types.FunctionType
print(type(lambda x: x))
# Test types.LambdaType
print(type(lambda x: x))
# Test types.GeneratorType
print(type(lambda x: x))
# Test types.CodeType
print(type(lambda x: x).__code__)
# Test types.TracebackType
try:
    raise Exception
except Exception as e:
    print(type(e.__traceback__))
# Test types.FrameType
try:
    raise Exception
except Exception as e:
    print(type(e.__traceback__))
# Test types.DictProxyType
print(type(dict(a=1)))
# Test types.MethodType
class Foo:
    def bar(self):
        pass

print(type(Foo.__dict__['bar']))
# Test types.BuiltinMethodType
print(type(list.append))
# Test types.UnboundMethodType
print(type(list.append))
# Test types.MemberDescriptorType
print(type(Foo.__dict__['bar']))

