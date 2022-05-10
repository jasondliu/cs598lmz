from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

def test():
    print('test')

print(isinstance(test, FunctionType))

import types
print(isinstance(test, types.FunctionType))

import types
print(isinstance(test, types.GeneratorType))

print(isinstance(a, types.GeneratorType))

print(isinstance(a, types.FunctionType))

print(isinstance(a, types.LambdaType))

print(isinstance(a, types.CodeType))

import types
print(isinstance(a, types.TracebackType))

import types
print(isinstance(a, types.FrameType))

import types
print(isinstance(a, types.BufferType))

import types
print(isinstance(a, types.DictProxyType))

import types
print(isinstance(a, types.GetSetDescriptorType))

import types
print(isinstance(a, types.MemberDescriptorType))

import types
print(isinstance(a, types
