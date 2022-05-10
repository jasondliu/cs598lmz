import io
class File(io.RawIOBase):
    def _init_(self,content,filename='hello.txt',
               mode='w+',encoding='utf-8'):
        self.content = content
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
file = File('hello world')
print(file.read())

class Person:
    name = "张三"
    def printNmae(self):
        print(self.name)
class Student(Person):
    pass
s1 = Student()
s1.printNmae()
print(issubclass(Student,Person))
print(isinstance(s1,Student))
print(isinstance(s1,Person))
delattr(Person,'name')
print(Person.__dict__)#添加，删除类中属性
Person.name = '王五'
print(Person.__dict__)
print(getattr(Person,'age',18))#获得类属性
print(hasattr(Person,'
