fn = lambda: None
# Test fn.__code__   作用如同fn.__code__.co_filename
# 在Python3中会报错
try:
    result = fn.__code__.co_filename
except:
    pass
else:
    result = fn.__code__.co_filename.split('/')[-1].split('.')[0]

assert result == 'chapter10', "Failed assert... result is %s." % result


# 编写一个函数，设置它的两个默认参数为0和0，并返回他们的和
def sumc(*args):
    args_00, args_01 = 0, 0
    n = len(args)
    if n == 0:
        return args_00 + args_01
    elif n == 1:
        args_00, args_01 = args[0], args_01
        return args_00 + args_01
   
