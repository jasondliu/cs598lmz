from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">i")
s.size
# 4

# 在给定模块中查找带有特定名称的对象
# getattr(object, name[, default])
# 获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选
getattr(s, 'size')
# 4
getattr(s, 'format')
# '>i'
getattr(s, 'unpack')
# <bound method Struct.unpack of >i>

# hasattr(object, name)
# 判断对象object里面是否有name属性或者
