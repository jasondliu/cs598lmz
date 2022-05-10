import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
# https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
class Test:
    def __del__(self):
        print('deleted')

t = Test()
del t

#%%
# https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
class Test:
    def __del__(self):
        print('deleted')

t = Test()
t.__del__()

#%%
# https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object
class Test:
    def __del__(self):
        print('deleted')

t = Test()
t.__del__()
del t

#%%
# https://stackoverflow.com/questions/865115/how-do-i-correct
