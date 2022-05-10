import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
print('gc: Collecting with strong refs =', gc.collect())

def show_details(message, ob_list):
    print(message)
    print('  len(ob_list) =', len(ob_list))
    print('  list refers to:', [id(o) for o in ob_list])
    print('  ob_list[0] refers to:', id(ob_list[0]))

r1 = WeakList()
print('r1: id(), type(), len(), str() =', id(r1), type(r1), len(r1), r1)

# Show details for list objects (normal lists)
show_details('gc: initial condition:', gc.get_objects())

# Build a list of objects to be tracked
# Build a list of things
num_objs = 10
for i in range(num_objs):
    obj = AnObject()
    # Note that we add the object to the weak list, but
    # it will not be reference counted
    r1.add_object(obj)


