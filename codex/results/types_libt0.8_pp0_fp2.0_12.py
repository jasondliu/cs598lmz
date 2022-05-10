import types
types.MethodType(f, None, Spam)  # Function is bound to Null
# <bound method Spam.f of <class '__main__.Spam'>>
s = Spam()  # Function is bound to instance
types.MethodType(f, s, Spam)  # Function is bound to instance
# <bound method Spam.f of <__main__.Spam object at 0x00E95E90>>
types.MethodType(f, s)  # Can also attach to instances
# <bound method Spam.f of <__main__.Spam object at 0x00E95E90>>
s.method = types.MethodType(f, s)  # Attach as name in instance
s.method()  # Call method through instance
# 0x00E95E90
s.method = f  # Rebind the method to the instance
s.method()
# <__main__.Spam object at 0x00E95E90>
Spam.method(s)  # Same as previous line (via instance)
# <__main__.Spam object at 0x00
