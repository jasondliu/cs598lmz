import types
types.ClassType
types.FunctionType
types.GeneratorType
types.LambdaType
types.ModuleType
types.TypeType
types.TracebackType
types.UnboundMethodType
types.FrameType
types.BufferType
types.DictProxyType
types.NotImplementedType
types.GetSetDescriptorType
types.MemberDescriptorType
types.EllipsisType
types.SliceType
types.BuiltinFunctionType
types.BuiltinMethodType
types.MethodType
types.CodeType
types.UnicodeType
types.StringType
types.XRangeType
"""

def get_content(path):
    with open(path) as f:
        return f.read()


def get_answer(path):
    return map(int, get_content(path).split())


if __name__ == '__main__':
    path = raw_input()
    # path1 = r'''c:\users\wangchao\desktop\pc\QQ\d6.txt'''
    print get_content(path)
