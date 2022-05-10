import ctypes
ctypes.cast(id(a), ctypes.py_object).value

#%%
##python中的gc
import gc
class A(object):
    def __del__(self):
        print 'del...'
        
a=A()
b=A()
c=A()

del a
del b
del c
gc.collect()

#%%
import gc,sys
class B(object):
    def __del__(self):
        print 'del......'
        
del B
gc.collect()
print sys.getrefcount(B)
b=B()
print sys.getrefcount(b)

print 
print

#%%
import gc,sys
print gc.get_threshold()

gc.set_threshold(700,10,5)
print gc.get_threshold()

#%%
##对象在内存中的分配过程
#内置对象所在的内存，一开
