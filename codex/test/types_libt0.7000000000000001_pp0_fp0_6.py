import types
types.MethodType(func, group, Group)

group.print_name()

# 给实例绑定的方法，对另一个实例是不起作用的
member = Member('Tom', 18)
member.print_name()


# 给类中添加方法，对所有实例都起作用
def set_name(self, name):
    self.name = name

Group.set_name = set_name

group.set_name('Chen')
print(group.name)

member.set_name('Wang')
print(member.name)
