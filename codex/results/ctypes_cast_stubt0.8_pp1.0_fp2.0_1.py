import ctypes
ctypes.cast(x, ctypes.py_object).value = 0
print(x)

'''
print(dir(x))
print(dir(x))
'''
'''
a = getattr(x, '__yaml_add_representer__')
print('a =', a)

#print('a.func =', a.func)
print('a.__self__ =', a.__self__)
print('a.__self__ =', a.__self__)

a.__self__.__yaml_add_representer__(x, a)

print('x =', x)

'''
'''
try:
    x.__yaml_add_representer__()
except Exception as e:
    print(e)
finally:
    print('finally')

print('x =', x)

'''
'''
print('helpers.yaml_add_representer =', helpers.yaml_add_representer)

#helpers.yaml_add_representer(x, x.__yaml_
