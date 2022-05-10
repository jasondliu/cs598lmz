import types
types.MethodType(lambda self: self.name, None, Employee)

# 测试:
bart = Employee('Bart', 'male', 36, '637-27-1234', '123@gmail.com', 'Engineer')
print(bart.name)
print(bart.email)
bart.get_job()

# 测试:
lisa = Employee('Lisa', 'female', 28, '532-89-2345', 'lisa@qq.com', 'Engineer')
bart.get_job()

print('%s: %s' % (Employee.get_job.__name__, Employee.get_job.__doc__))
print('%s: %s' % (bart.get_job.__name__, bart.get_job.__doc__))
