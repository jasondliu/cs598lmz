import types
types.MethodType

class Person:
   
    def set_age(self, age):
        self.age = age
        
    def get_age(self):
        return self.age
       
        
person = Person()
print(person)
print(person.age)
print(person.get_age())

person.set_age(45)
print(person.get_age())

print("___add new method over the existing class")
def set_city(self,city):
    self.city = city
   
def get_city(self):
    return self.city
   
print("person.city ", person.city)
