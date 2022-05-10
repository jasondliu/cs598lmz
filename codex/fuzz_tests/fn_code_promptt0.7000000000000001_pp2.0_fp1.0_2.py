fn = lambda: None
# Test fn.__code__.co_stacksize
fn.__code__.co_stacksize

"""
分析：

- 函数的__name__属性表示调用函数时的名字
- 函数的__doc__属性表示文档字符串
- 函数的__defaults__属性表示默认参数的值
- 函数的__code__属性表示函数的字节码对象
- 函数的__closure__属性表示函数的闭包
- 函数的__dict__属性表示函数的属性字典
- 函数的__globals__
