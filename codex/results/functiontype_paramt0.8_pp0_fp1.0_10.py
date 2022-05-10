from types import FunctionType
list(FunctionType([],[]))

#You can always delete an attribute
del w.name
w.name
dir(w)
 
#You can also delete a method (You CANNOT delete a function you can only delete a method)
#del w.get_name
#w.get_name

#You can add a new class attribute
w.address = "United States"
w.address

#You can also add a new function attribute
def get_age(self):
    return self.age
w.get_age = get_age
w.get_age()

#You can see that the get_age method is now part of dir(w)
dir(w)
 
#It can be deleted like any other attribute
del w.get_age
