gi = (i for i in ())
# Test gi.gi_code.co_filename
gi.gi_code.co_filename
# Test gi.gi_frame.f_code.co_filename
gi.gi_frame.f_code.co_filename
# Test gi.gi_frame.f_code
gi.gi_frame.f_code

# Test function attributes
def func():
    pass
func.__code__
func.__code__.co_filename
func.__code__.co_name
func.__code__.co_firstlineno
func.__code__.co_argcount
func.__code__.co_varnames
func.__code__.co_names
func.__code__.co_flags
func.__code__.co_lnotab

# Test method attributes
class C:
    def meth(self):
        pass
C.meth.__func__
C.meth.__func__.__code__
C.meth.__func__.__code__.co_filename
C.meth.__func__.__code__.co_name
C.meth
