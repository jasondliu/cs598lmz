fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__
# 
# class A(object):
#     def __init__(self, x):
#         self.x = x
#     def __call__(self, y):
#         return self.x + y
# 
# a = A(1)
# b = A(2)
# a.__call__(2)
# b.__call__(3)
# 
# a.__code__ = b.__code__
# a(2)
# b(3)
# 
# # __call__
# a.__call__ = b.__call__
# a(2)
# b(3)
# 
# 
# # __dict__
# a.__dict__ = b.__dict__
# a(2)
# b(3)
# 
# # __class__
# a.__class__ = b.__class__
# a(2)
# b(3)
# 
# 
# # __dict__
# a.__dict__ = b
