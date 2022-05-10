from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你想要通过某个类创建实例并且还希望在创建实例的时候改变一些类或实例的属性，可以使用定制的 metaclass。
# 为了演示这个，下面这个例子演示了怎样去定义一个元类，以及它是如何被使用的。
# 定义 ListMetaclass，按照默认习惯，metaclass 的类名总是以 Metaclass
