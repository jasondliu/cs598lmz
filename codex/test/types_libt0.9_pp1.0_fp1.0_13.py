import types
types.MethodType(local_f,None,Demo)

demo = Demo()
demo.local_f()

print('------------------删除实例方法----------------------')

del demo.local_f

print('------------------类中定义私有方法----------------------')

#类中定义的方法名称开头两个下划线代表类的私有方法
#被私有后的方法只能在定义时所在的类中访问

class DemoPrivate(object):
    def __private_f(self):
        print('类的私有方法')

demo = DemoPrivate()
#demo.__private_f()
#DemoPrivate.__private_f(demo)
#这样不是私有的
