import types
types.ClassType

# classes can inherit from other classes
class Car(object):
    "Generic car class"
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return "Car: "+self.name

class Tesla(Car):
    "Subclass of Car"    
    def __init__(self, name="Leaf", model="Leaf"):
        # call base class constructor
        Car.__init__(self, name)
        self.model = model
    def get_name(self):
        # you can always access base class methods
        return "Tesla: "+Car.get_name(self)

# Car still works
c = Car("VW")
