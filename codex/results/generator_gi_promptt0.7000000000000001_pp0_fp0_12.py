gi = (i for i in ())
# Test gi.gi_code.co_filename
gi.gi_code.co_filename
# Test gi.gi_frame.f_code.co_filename
gi.gi_frame.f_code.co_filename
# Test gi.gi_frame.f_back.f_code.co_filename
gi.gi_frame.f_back.f_code.co_filename

# Test that we can access a property
import abc
abc.ABCMeta.__abstractmethods__

# Test that we can access a method
abc.ABCMeta.__instancecheck__
# Test that we can access the __name__ attribute
abc.ABCMeta.__instancecheck__.__name__

# Test that we can access the __qualname__ attribute
abc.ABCMeta.__instancecheck__.__qualname__

# Test that we can access the __code__ attribute
abc.ABCMeta.__instancecheck__.__code__

# Test that we can access the __code__.co_filename attribute
abc.ABCMeta.__instancecheck__.__code__.co_filename

# Test that we can access
