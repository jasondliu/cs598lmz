from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# __new__() 方法接受一个参数 cls ，代表要实例化的类，此参数在实例化时由 Python 解释器自动提供(例如下文的 MyList 和 MyDict )。
# 如果你希望你的类能支持像 list 那样的列表推导式，你就得自己写一个 __iter__() 方法，该方法返回一个迭代对象，然后 Python 的 for 循环就会不断调用该
