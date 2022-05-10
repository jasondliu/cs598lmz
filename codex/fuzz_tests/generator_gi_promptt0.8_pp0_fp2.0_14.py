gi = (i for i in ())
# Test gi.gi_code.co_filename
# Test gi.gi_code.co_firstlineno
# Test gi.gi_frame.f_code.co_filename
# Test gi.gi_frame.f_code.co_firstlineno
# Test gi.__name__
# Test sys._getframe().f_code.co_filename
# Test sys._getframe().f_code.co_firstlineno
print 1
# Test sys._getframe().f_back.f_code.co_filename
# Test sys._getframe().f_back.f_code.co_firstlineno
def f():
    print 2
    # Test sys._getframe().f_code.co_filename
    # Test sys._getframe().f_code.co_firstlineno
    # Test sys._getframe().f_back.f_code.co_filename
    # Test sys._getframe().f_back.f_code.co_firstlineno
    # Test sys._getframe().f_back.f_back.f_code.co_filename
    # Test sys._getframe
