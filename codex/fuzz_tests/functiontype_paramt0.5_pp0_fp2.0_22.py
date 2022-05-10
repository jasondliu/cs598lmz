from types import FunctionType
list(FunctionType(lambda x:x,globals(),'foo'))

# 下面这个是一个无效的创建方式
# lambda x:x
# 下面这个是一个有效的创建方式
# lambda:None

# 下面这个是一个有效的创建方式
# lambda x,y=1,*z:z

# 下面这个是一个有效的创建方式
# lambda x,y=1,*z,**t:t

# 我们通过下面的方式来创建一个函数
def foo():
    pass

# 我们通过下面的方式来创建一个函数
foo=lambda x:
