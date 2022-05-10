import types
types.FunctionType,types.LambdaType,types.ModuleType
types.BuiltinFunctionType,types.BuiltinMethodType,types.GeneratorType,
types.MethodType,types.TracebackType,types.FrameType,types.CodeType

import tkinter
class Averager:
    def __init__(self):
        self.series = []
    def __call__(self,new_value):
#调用方法相当于执行类中的__call__函数
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

# 属性调用
def __getattr__(self, name):
    return getattr(self._obj,name)
# __getattribute__如果类定义了这个方法，则属性的获取操作总是会调
