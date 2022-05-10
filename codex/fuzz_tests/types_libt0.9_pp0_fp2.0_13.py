import types
types.MethodType(test_05, list)

# getattr 让别人取得你的属性
# setattr 设置你的属性

class Personal:
    def __init__(self, name, age, id, sex, height=175):
        self.name = name
        self.age = age
        self.__id = id
        self.sex = sex
        self.height = height
        self.__class__.height = height

    def __str__(self):
        return "{}__{}".format(self.name, self.height)

    def display(self):
        print(self.__class__.__name__)


p1 = Personal('tom', 22, 2, 'male')
print(getattr(p1, "name"))

# setattr 两个参数
setattr(p1, 'height', 160)
p1.display()

# hasattr
hasattr(p1, 'name')

class Phone:
    def
