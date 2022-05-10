import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
objects = []
for i in range(10):
    objects.append(dict())                              # modify this to use your Student class
    objects.append([])
    objects.append(set())
gc.collect()
s = sum(sys.getrefcount(o) for o in objects)
print(s)

del objects                                            # get rid of the list
gc.collect()
print(len(gc.garbage))
print(gc.garbage[2])
#print(gc.garbage[2].__dict__)
print(gc.garbage[2].__weakref__.data)


# Modify the Student class so that students are weakly referenced and the number of students currently enrolled
# can be obtained by calling gc.collect()
# Test this function with the code below

# Test the new class here
