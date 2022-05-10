from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 注意，这里的s是一个类，不是实例

# 在类中定义类方法
# 类方法的第一个参数是cls，而不是self
class Spam:
    @classmethod
    def grok(cls):
        print('Spam.grok')

Spam.grok()

# 在类中定义静态方法
# 静态方法没有参数
class Spam:
    @staticmethod
    def grok():
        print('Spam.grok')

Spam.grok()

# 在类中定义属性
