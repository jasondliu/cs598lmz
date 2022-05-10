import types
# Test types.FunctionType
print(type(abs))

# Test types.LambdaType
print(type(lambda x: x))

# Test types.GeneratorType
print(type((x for x in range(10))))

# Test types.GeneratorType
print(type(x for x in range(10)))

# Test types.GeneratorType
print(type((x for x in range(10))))

# Test types.BuiltinFunctionType
print(type(cmp))

# Test types.BuiltinMethodType
print(type([].append))

# Test types.UnboundMethodType
print(type(str.upper))

# Test types.MethodType
print(type([].append))


# -*- coding:utf-8 -*-

def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello()
print(
