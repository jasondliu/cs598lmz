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
person1 = Person()
person1.set_city("kiev")
person1.set_age(42)
print("person1.city ", person1.city)

person1.set_city_100 = types.MethodType(set_city, person1) #or - setattr(person1, "set_city_100", types.MethodType(set_city, person1))
person1.get_city_100 = types.
