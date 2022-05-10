from types import FunctionType
list(FunctionType(lambda x:x+1,{}).__code__.co_varnames)

#%%
#调用函数
#调用函数时，会为函数创建一个新的执行环境，在这个环境中，函数所需的变量都将被创建
#在函数执行完毕后，这个环境将被销毁

#%%
#全局变量和局部变量
#在函数内部可以访问全局变量，但是不能修改它的值
#在函数内部
