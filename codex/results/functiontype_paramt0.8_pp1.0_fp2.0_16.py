from types import FunctionType
list(FunctionType(lambda x, y: x*y, globals(), 'myfunc')(3, 3))
 

print(list(chain(*test_list)))

print(globals())


# %%
liste = [1,2,3]

liste


# %%
def f(y):
    return y+2

def f_prime(y):
    return y+2
    
    
    
    
    
    
class TestClass(object):

    def __init__(self, x, y=1):
        self.x = x
        self.y = y
        self.z = 0
        
    def __repr__(self):
        return f'TestClass(x={self.x}, y={self.y}, z={self.z})'
    
    def f(self):
        return self.x*self.x
    
    def g(self):
        return self.x*self.y
    
    def h(self):
        return self.x+self.y
    
    def i(self):
       
