import ctypes
ctypes.cast(pointer, ctypes.py_object).value
# with 'as'
try:
    pass
except Exception as ex:
    print(ex, type(ex))
 
# without 'as'
try:
    pass
except Exception, ex:
    print(ex, type(ex))
 
# another try
try:
    pass
except Exception:
    ex = sys.exc_info()[0]
    print(ex)
    
    
    
    
    
    
    
    
    
    '''
    Exception handling
    '''
    try:
        # All statements that may raise an exception
    except Exception:
        # All statements that will be executed if exception is raised in try block
    finally:
        # All statements that will be executed irrespective of try block execution
    else:
        # All statements that will be executed only if try block executes successfully
 
 
try:
    raise ValueError("Error")
except Exception as e:
    print e.__class__.__name__
    print e  # This will print full traceback
    print e.
