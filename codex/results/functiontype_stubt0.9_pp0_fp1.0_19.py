from types import FunctionType
a = (x for x in [1])
if isinstance(a, FunctionType):
    print('yes')
else:
    print("no")

print(type(a))

print("#################")

# 注意：不要混淆类型和类！
# 面向对象的程序设计师累了讲述概念：类是抽象的模板，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# 一个山羊拥有山
