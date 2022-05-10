from types import FunctionType
list(FunctionType(f.__code__, globals(), 'fn').__closure__)

# 可以看到这个函数的__closure__中存储了一个cell对象，这个对象有一个cell_contents属性，这个属性的值就是外部作用域的变量x的值
# 这个cell对象就是用来存储闭包中的变量的值的。
# 一个函数的__closure__属性中可能会存在多个cell对象，每个cell对象对应一个外部作用域的变量
# 这个cell对象就是用
