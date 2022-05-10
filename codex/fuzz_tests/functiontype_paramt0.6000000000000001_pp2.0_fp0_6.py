from types import FunctionType
list(FunctionType(lambda x:x,globals(),'lambda'))

#%%
#
#   内置函数
#

#%%
#
#   1.求值函数
#       布尔函数：bool，用来判断对象是否为True或False
print(bool())
print(bool(0))
print(bool(None))
print(bool(''))

#%%
#       常用函数：all,any，用来判断对象是否为True或False
print(all([0,1,2]))
print(all([0,1,2,3]))
print(all([0,1,2,None]))
print(all([]))

print(any([0,1,2]))
print(any([0,1,2,3]))
print(any([0,1,2,None
