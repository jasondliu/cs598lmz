import types
# Test types.FunctionType and types.LambdaType

def f(): pass
def g():
    def f(): pass

#f = lambda: 1

import types


# On 2.6, isinstance(getattr(types, str(x)), types.FunctionType)
# is True for x in ('FunctionType', 'LambdaType', 'BuiltinFunctionType',
# 'BuiltinMethodType', 'MethodType')
for x in dir(types):
    if x.endswith('Type'):
        print x, isinstance(f, getattr(types, x))
# FunctionType True
# LambdaType False
# MethodType False
# BuiltinFunctionType True
# BuiltinMethodType False
# CodeType False
# TypeType False
# TracebackType False
# FrameType False
# GetSetDescriptorType False
# MemberDescriptorType False
