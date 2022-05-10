from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 使用map()函数创建一个新的列表
values = [1, 4, 9, 16, 25]
map(lambda x: x * 2, values)

# 使用filter()函数创建一个新的列表
values = [1, 2, 3, 4, 5, 6]
filter(lambda x: x % 2 == 0, values)

# 使用reduce()函数创建一个新的列表
values = [1, 2, 3, 4, 5]
reduce(lambda x, y: x * y, values)

# 将函数作为参数传递给另一个函数
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)
    # Invoke the callback with the result
    callback(result)
