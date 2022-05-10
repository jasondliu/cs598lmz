fn = lambda: None
# Test fn.__code__
#print(fn.__code__)
#print(fn.__code__.co_filename)
#print(fn.__code__.co_name)


# 警告的处理
#import warnings
#def fxn():
#	warnings.warn("deprecated", DeprecationWarning)
#with warnings.catch_warnings(record=True) as w:
#	warnings.simplefilter("always")
#	fxn()
#	print(w[-1].message)
#	print(w[-1].category)
#
#print(w)
# print(w[0].message)
# print(w[0].category)
#print(w[-1].message)
#print(w[-1].category)

# import sys
# import warnings
# def fxn():
# 	warnings.warn("deprecated", DeprecationWarning)
# def showwarning(*args, **kwargs):
# 	print("args = ", args)
# 	print("kwargs = ", kwargs
