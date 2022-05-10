import ctypes
ctypes.cast(id(int), ctypes.py_object).value

#@title
#%%writefile -a {folder}/{name}.py

def get_id(x):
  return ctypes.cast(id(x), ctypes.py_object).value

#@title
#%%writefile -a {folder}/{name}.py

class id_dict(dict):
  def __missing__(self, key):
    self[key] = value = len(self)
    return value

#@title
#%%writefile -a {folder}/{name}.py

class nb_dict(dict):
  def __missing__(self, key):
    self[key] = value = key.__name__ + '_' + str(len(self))
    return value

#@title
#%%writefile -a {folder}/{name}.py

_id_dict = id_dict()
_nb_dict = nb_dict()

#@title
#%%writefile -a {folder}/{name}.py

def _get
