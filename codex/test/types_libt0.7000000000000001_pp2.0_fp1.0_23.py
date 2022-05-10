import types
types.MethodType

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def displayEmployee(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
        
    def print_info(self):
        print("The info is: ")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salary: ",self.salary)
    
    def set_name(self,name):
        self.name = name
    
    def set_age(self,age):
        self.age = age
    
    def set_salary(self,salary):
        self.salary = salary
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
