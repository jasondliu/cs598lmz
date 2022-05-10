import gc, weakref, time

#----------------------clear_object_ref()----------------------------------------
def clear_object_ref():
    obj_id = id(obj_dict)
    obj_id_hex = hex(obj_id)
