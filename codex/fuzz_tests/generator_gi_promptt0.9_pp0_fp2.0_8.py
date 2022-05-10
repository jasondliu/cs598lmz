gi = (i for i in ())
# Test gi.gi_code.co_name
gi.gi_code.co_name


# These are useful to note
is_generator = lambda o: (type(o) is generator) or inspect.isgenerator(o)
'''
>>> o = (i for i in ())
>>> type(o)
<type 'generator'>
>>> import inspect
>>> inspect.isgenerator(o)
True
'''
