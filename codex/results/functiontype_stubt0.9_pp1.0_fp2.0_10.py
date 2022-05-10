from types import FunctionType
a = (x for x in [1])
b = list(x for x in [2])
c = dict((x,x) for x in [3])
d = set(x for x in [4])
e = tuple(x for x in [5])
f = FunctionType((),"")


#内置函数type 用来检查对象类型
type(1) #整数
type(1.0) #浮点数
type(obj) is ClassType #class obj 是否实例化自ClassType
type(obj) == ClassType #是否是class obj
type(obj) in ClassTuple #class obj 是否实例化自ClassTuple的其中一个类
isinstance(obj, ClassType) #等同于 type(obj) is ClassType
issubclass(sub, super)


type('a'), type(b'a'), type(bytearray('
