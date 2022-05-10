import gc, weakref, time

#----------------------clear_object_ref()----------------------------------------
def clear_object_ref():
    obj_id = id(obj_dict)
    obj_id_hex = hex(obj_id)
    print obj_id_hex
    del obj_dict
    obj_dict = {}
    gc.collect()

#----------------------main()----------------------------------------

obj_dict = {}
for i in xrange(10000):
    tmp_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    obj_dict[tmp_str] = tmp_str

obj_id = id(obj_dict)
obj_id_hex = hex(obj_id)
print obj_id_hex
obj_ref = weakref.ref(obj_dict)
print obj_ref
print obj_ref()

clear_object_ref()
print obj_ref()

time.sleep(100)
