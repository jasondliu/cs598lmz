import types
types.MethodType(func, None, class_name)

# 实例方法
# 实例方法的第一个参数是self，self代表的是类的实例，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
# self不是python关键字，换成其他的也是可以的。
# 但是最好还是按照约定是用self。
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

# 类的方法与普通的函数只
