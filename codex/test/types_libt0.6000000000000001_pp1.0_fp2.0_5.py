import types
types.MethodType(func,None,Spam)

class Spam:
    pass
def func(self):
    print('hello world')
# Spam.method=func

s=Spam()
s.method()
