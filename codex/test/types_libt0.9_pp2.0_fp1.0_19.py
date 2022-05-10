import types
types.CodeType = None  # Don't allow CodeType()
types.FunctionType = None  # Don't allow FunctionType()
types.BuiltinFunctionType = None  # Don't allow BuiltinFunctionType()
types.GeneratorType = None  # Don't allow GeneratorType()
types.MethodType = None  # Don't allow MethodType()


class DontPermit(object):

    def __enter__(self):
        pass

    def __exit__(self, et, eo, tb):
        pass


# from: https://stackoverflow.com/questions/3910083/python-how-to-disable-popen-calls-under-windows
