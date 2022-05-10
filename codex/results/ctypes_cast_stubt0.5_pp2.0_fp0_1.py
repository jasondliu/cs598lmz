import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%

class MyClass:
    def __init__(self):
        self.x = 5
        self.y = 10
        self.z = 20
        self.a = 30
        self.b = 40
        
    def __getitem__(self, key):
        if key == 'x':
            return self.x
        elif key == 'y':
            return self.y
        elif key == 'z':
            return self.z
        elif key == 'a':
            return self.a
        elif key == 'b':
            return self.b
        else:
            raise KeyError(key)
    
    def __setitem__(self, key, value):
        if key == 'x':
            self.x = value
        elif key == 'y':
            self.y = value
        elif key == 'z':
            self.z = value
        elif key == 'a':
            self.a = value
        elif key == 'b':

