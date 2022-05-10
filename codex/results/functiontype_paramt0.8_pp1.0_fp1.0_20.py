from types import FunctionType
list(FunctionType(c,globals(),'my_func'))

#%%

def my_generator():
    n = 1
    print('This is printed first') # 1
    # Generator function contains yield statements
    yield n
    
    n += 1
    print('This is printed second') # 2
    yield n
    
    n += 1
    print('This is printed at last') # 3
    yield n
        
a = my_generator() # a: generator object
next(a)
next(a)
next(a)
next(a)
