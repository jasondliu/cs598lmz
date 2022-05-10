import types
types.new_class('Person')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __hash__(self):
        return hash(self.age)
    
    def __call__(self, *args, **kwargs):
        print(f"{self.name} is now calling you")
    
    def __len__(self):
        return self.age
    
    def __getitem__(self, index):
        return self.name[index]
    
    def __setitem__(self, index, value):
       
