import types
types.MethodType(f, None, Student)

# 方法2：实例方法,使用类的实例绑定
s = Student()
def g(self):
	return 'g'

s.g = types.MethodType(g, s)
s.g()

class Student(object):
	count=0
	def __init__(self,name):
		self.name = name
		Student.count += 1

# 测试:
if Student.count != 0:
    print('测试失败1!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败2!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student.count)
            print('测试
