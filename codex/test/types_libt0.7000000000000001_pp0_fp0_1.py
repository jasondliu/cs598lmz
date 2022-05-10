import types
types.ClassType

# インスタンス宣言
class User:
    pass

print(type(User))
# <class 'type'>

tom = User()
print(type(tom))
# <class '__main__.User'>

# クラス変数
class User:
    count = 0

print(User.count)
# 0

User.count += 1
print(User.count)
# 1

print(dir(User))
print(dir(tom))

# インスタンス変数
class User:
    def __init__(self, name):
        self.name = name
        print("{} is initialized".format(self.name))

bob = User("Bob")
# Bob is initialized
print(bob.name)
# Bob

tom = User("Tom")
# Tom is initialized
print(tom.name)
# Tom

# インスタンスメソッド
