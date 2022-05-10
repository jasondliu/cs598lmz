from types import FunctionType
list(FunctionType(add,globals())('1','2','3','4','5'))

#%%
from types import FunctionType
def add(a,b,c,d,e):
    return(a+b+c+d+e)
list(FunctionType(add,globals())('1','2','3','4','5'))

#%% [markdown]
# ## Partial 绑定（柯里化特征）
# 利用参数，给函数中的一些参数默认值，返回一个新的函数
# 即这个新的函数可以接受其他参数
#%%
# 利用 partial(name,arg1,arg2,....) 函数将函数name中arg1,arg2等参数设
