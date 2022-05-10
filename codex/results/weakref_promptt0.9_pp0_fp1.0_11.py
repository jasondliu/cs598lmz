import weakref
# Test weakref.ref by keeping a cache of objects
class Myclass:
     #def __init__(self):
     #     Myclass.all_objects.add(weakref.ref(self))  # Add a new weak reference
     def __del__(self):
         print "Deleted"
#Myclass.all_objects = set() 
        
a=Myclass()
print a  # Myclass instance
del a  # Deletes the object
raw_input()
