fn = lambda: None
# Test fn.__code__.co_varnames and fn.__code__.co_argcount
print fn.__code__.co_varnames # ()
print fn.__code__.co_argcount # 0

# Test name of module
print fn.__code__.co_name # <lambda>
print fn.__code__.co_filename # <stdin>
print "__code__.co_filename =", os.path.basename(fn.__code__.co_filename)
''' Test the file name from which function was loaded '''
# Create a file module1.py
'''
def fn():
    pass
'''
# Add paths
import sys
sys.path.append('..')
print sys.path
# Import file
import module1
print dir(module1)
print module1.fn.__code__.co_filename
print os.path.basename(module1.fn.__code__.co_filename)

# Get module from stack trace
import traceback
def get_module_run_from_traceback():
    return traceback.extract_
