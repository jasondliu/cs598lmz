import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)

# Get the necessary functions and objects in scope
cfun = ctypes.CDLL(os.environ['FULL_LIB'])
Object = cfun.Object
Object_new = cfun.Object_new
#The functions below set the data pointer
Object_set_data = cfun.Object_set_data
Object_get_data = cfun.Object_get_data
Object_wipe = cfun.Object_wipe
# Object_get_class(Object*) -> (Class*)
Object_get_class = cfun.Object_get_class
Class_get_name = cfun.Class_get_name
# Get Item at position index from the Aqt.Array/List.
Object_get_item = cfun.Object_get_item
Object_set_item = cfun.Object_set_item
Object_get_meta_item = cfun.Object_get_meta_item
Object_set_meta_item = cfun.Object_set_meta_item
Object_call = cfun.Object_call
Object_cast = cfun
