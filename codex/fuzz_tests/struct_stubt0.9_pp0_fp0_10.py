from _struct import Struct
s = Struct.__new__(Struct)
s.size = 5
decode("test", s)
%timeit decode("test", s)

# As before, _struct (via the C implementation) is significantly faster.
# 
# Final Thoughts
# =============
# 
# In this post, we have looked at how to decode binary data to Python. In the next post, we'll look at encoding Python data to binary.
# 
# Knowing what I know about Python, the implementation of the functions here is probably going to be very wrong in the style of Python. I welcome any corrections or improvements.

# ![](http://www.python-course.eu/images/adverts/python_weekly.gif)
