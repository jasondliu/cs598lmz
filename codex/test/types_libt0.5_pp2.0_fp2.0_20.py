import types
types.MethodType(func,None,A1)

class A2(object):
    pass

a2 = A2()
a2.__dict__
a2.func = func
a2.__dict__
a2.func()

class A3(object):
    def func(self):
        print('A3.func')

a3 = A3()
a3.func()

class A4(object):
    def func(self):
        print('A4.func')

a4 = A4()
a4.func()
a4.func = types.MethodType(func,a4)
a4.func()
a4.func = func
a4.func()

class A5(object):
    def func(self):
        print('A5.func')

a5 = A5()
a5.func()
a5.func = types.MethodType(func,a5,A5)
a5.func()
a5.func = func
a5.func()

