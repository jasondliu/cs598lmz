import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    """Ha ha ha, I'm a useless callback!"""
    return True


api = com.find_api('gem')
api.assign_callback(fun)
hello = com.py_load(api)
api.call('Hello', (hello,))
api.call('SetCallback', (hello, fun))
print api.call('Hello', (hello,))
print api.call('GetCallback', (hello,))

print 'Start python callback:'
if api.call('HelloWithCallback', (hello,), callback=True):
    print 'Python: yeah! Was I useful?'

print 'Let C++ callback:'
api.call('HelloWithCallback', (hello,))


print 'Reset python callback:'
api.call('SetCallback', (hello, None))
api.call('HelloWithCallback', (hello,))
