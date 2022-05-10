import types
types.MethodType(func, None, class_name)
# class_name.func = types.MethodType(func, class_name)

# 实例方法
# 实例方法的第一个参数是self，它代表的是类的实例，self在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。
# self不是python关键字，我们把他换成runoob也是可以正常执行的
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test()
t.prt()

