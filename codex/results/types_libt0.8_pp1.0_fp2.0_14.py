import types
types.MethodType(lambda *_: True, my_object)

print(my_object.get_message)
print(my_object.get_message())

class MyClass:
    def __init__(self):
        self.number = 10
        self.__secret_number = 5
        
instance = MyClass()
print(instance.number) # 10
print(instance.__secret_number) # AttributeError: 'MyClass' object has no attribute '__secret_number'

class MyClass:
    def __init__(self):
        self.number = 10
        self.__secret_number = 5
        
    def get_secret_number(self):
        return self.__secret_number
    
instance = MyClass()
print(instance.number) # 10
print(instance.get_secret_number()) # 5

class MyClass:
    def __init__(self):
        self.number = 10
        self.__secret_number = 5
        
    def get_secret_number(self):
        return self.__secret_number
    

