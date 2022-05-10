import gc, weakref

class Classic: pass

def f():
	obj = Classic()
	obj_id = id(obj)
	ref = weakref.ref(obj)
	obj.data = Classic()
	obj.data.data = Classic()

	o = ref()
	
	data_1 = obj.data is o.data
	data_2 = obj.data is o.data.data
	assert (data_1 and data_2) is False
	
	del obj
	gc.collect()
	assert ref() is None
	


#=====================
