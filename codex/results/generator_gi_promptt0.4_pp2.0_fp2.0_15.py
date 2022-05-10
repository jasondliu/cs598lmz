gi = (i for i in ())
# Test gi.gi_code.co_filename
print(gi.gi_code.co_filename)
# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_code.co_filename)
# Test gi.gi_frame.f_globals['__file__']
print(gi.gi_frame.f_globals['__file__'])
# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_code.co_filename)
print(gi.gi_frame.f_code.co_name)
print(gi.gi_frame.f_code.co_firstlineno)
print(gi.gi_frame.f_code.co_varnames)
print(gi.gi_frame.f_code.co_argcount)
print(gi.gi_frame.f_code.co_flags)

def f():
    print(sys._getframe().f_code.co_filename)
    print(sys._getframe().f_code.co_name)

