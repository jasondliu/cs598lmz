from types import FunctionType
a = (x for x in [1])
b = [1]
c = {1}
d = {1:1}
e = FunctionType(lambda x:x,globals())
f = type(e)
g = type(f)
print(type(a),type(b),type(c),type(d),type(e),type(f),type(g))

# type 可以创建类
# type(类名,父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
def upper_attr(future_class_name,future_class_parents,future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
