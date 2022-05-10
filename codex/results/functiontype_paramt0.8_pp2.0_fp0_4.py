from types import FunctionType
list(FunctionType('', '', '', '', '', '').__dict__.keys())

# 另一个提到的方法是使用inspect模块中的signature方法。它是通过解析函数的字节码实现的，在很多情况下比自己写的函数健壮性要好。
# 这里的例子是《Python Cookbook》第5版的示例，使用了不到一百行代码就实现了一个简单的函数签名查看工具。它支持默认参数、关键字参数、*和**
