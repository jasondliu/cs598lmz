import types
types.MethodType(myMethod,myObj)

# 先定义再绑定
def myMethod2(self):
    print('myMethod2')
myObj.myMethod2 = types.MethodType(myMethod2,myObj)
myObj.myMethod2()

# 通过type创建类
def say(self):
    print('say')

mySay = type('mySay',(object,),{'say':say})
mySay.say(mySay)

# 元类
class myMetaClass(type):
    def __new__(cls,className,baseClasses,attrs):
        print(cls)
        print(className)
        print(baseClasses)
        print(attrs)
        attrs['id']='123'
        return type.__new__(cls,className,baseClasses,attrs)

class myClass(object,metaclass=myMetaClass):
    name='123'
    age='234'
