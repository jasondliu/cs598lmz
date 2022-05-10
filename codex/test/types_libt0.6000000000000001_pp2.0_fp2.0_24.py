import types
types.new_class('MyClass', (object,), {'x': 10})

# 创建实例
inst = MyClass()
print('inst.x:',inst.x)

# 创建实例
inst2 = MyClass()
print('inst2.x:',inst2.x)

# 创建实例
inst3 = MyClass()
print('inst3.x:',inst3.x)

# 为类添加实例方法
def show_x(self):
    print(self.x)

MyClass.show_x = show_x
inst.show_x()
inst2.show_x()
inst3.show_x()

# 为类添加实例属性
MyClass.y = 100
print('inst.y:',inst.y)
print('inst2.y:',inst2.y)
