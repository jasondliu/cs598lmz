import ctypes
ctypes.cast(addr, ctypes.py_object).value

#%%
# load pickle file
import pickle

with open('data.pickle', 'rb') as file:
    data = pickle.load(file)

print(data)

#%%
# save pickle file
import pickle

data = {'a': [1, 2.0, 3, 4+6j],
        'b': ('string', u'Unicode string'),
        'c': None}

with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

#%%
# save pickle file
import numpy
import pickle

a = numpy.zeros((3,3,3))
b = numpy.ones((3,3,3))
c = numpy.eye(3)

with open('data.pickle', 'wb') as file:
    pickle.dump(a, file)
    pickle.dump(b, file)
    pickle.dump(c, file)

#%%
#
