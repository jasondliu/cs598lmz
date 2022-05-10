import types
types.MethodType(my_print2, obj)

obj.my_print3 = types.MethodType(my_print3, obj)
obj.my_print3()

def my_print4(self, param):
    print("instance method: %s, %s" % (self, param))

MyClass.my_print4 = types.MethodType(my_print4, None, MyClass)
obj.my_print4("test")

class MyClass2(object):
    pass

obj2 = MyClass2()
obj2.my_print4("test")

# classmethod
class MyClass3(object):
    @classmethod
    def my_print5(cls, param):
        print("class method: %s, %s" % (cls, param))

MyClass3.my_print5("test")
obj3 = MyClass3()
obj3.my_print5("test")
