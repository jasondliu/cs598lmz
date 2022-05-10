import types
types.MethodType(f,None,Hello)

# 实例属性和类属性
class Student(object):
    name = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name
print(s.name)

# 例外处理
try:
    print('try...')
    r = 10 / int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# 调用栈
def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

