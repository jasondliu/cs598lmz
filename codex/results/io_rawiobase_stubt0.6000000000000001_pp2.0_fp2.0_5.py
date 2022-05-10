import io
class File(io.RawIOBase):
    # ...

print(File.__bases__)

# <class 'io.RawIOBase'>

# 实例属性

# 实例属性实际上是一个字典，用于保存实例的属性

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         print('Woof!')

# d = Dog('Fido', 'German Shepherd')
# print(d.__dict__)

# {'name': 'Fido', 'breed': 'German Shepherd'}

# 我们可以通过给实例的 __dict__ 字典添加属性来为实例添加属性

# d
