from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2i'
s.size = 8
s.pack(1, 2)

# 一个非常简单的枚举类型
class Enum(object):
    def __init__(self, names):
        for number, name in enumerate(names.split()):
            setattr(self, name, number)

# 一个非常简单的通用枚举类型
class Enum(object):
    def __init__(self, **enums):
        self.__dict__.update(enums)

# 偏函数
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
