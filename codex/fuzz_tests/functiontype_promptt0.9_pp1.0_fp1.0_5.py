import types
# Test types.FunctionType
def function_type(obj):
    if isinstance(obj, types.FunctionType):
        print (obj.__name__)
    else:
        print ('not a function')

import inspect
# Test inspect.isclass
def is_class(obj):
    if inspect.isclass(obj):
        print ('it is a class.')
        print (obj.__qualname__)
    else:
        print ('it is not a class.')

# Test inspect.ismethod
def is_method(obj):
    if callable(obj) and hasattr(obj, '__call__'):
        print ('it is a method')
    else:
        print ('it is not a method')

from datetime import datetime
# Test format
def format_datetime(time=datetime.now()):
    print (time.strftime('%Y-%m-%d %H:%M:%S'))


from urllib import request
# test urllib.request.urlopen
def get_request(url):
    return request.url
