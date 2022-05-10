from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.unpack(b'\x00\x00\x00\x01')

# 如果你想通过某个类创建实例，并且还希望在实例创建之前改变类的某些属性，
# 那么你可以使用定义好的类来调用 type() 来创建出类
import operator
def named_tuple(classname, fieldnames):
    # Populate a dictionary of field property accessors
    cls_dict = {name: property(operator.itemgetter(n))
                for n, name in enumerate(fieldnames)}

    # Make a __new__ function and add to the class dict
