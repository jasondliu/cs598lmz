fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

#print('get_code_object')
#print(fn.__code__)

#print('get_code_object_co_name')
#print(fn.__code__.co_name)

#print('get_code_object_co_filename')
#print(fn.__code__.co_filename)

#print('get_code_object_co_firstlineno')
#print(fn.__code__.co_firstlineno)

#print('get_code_object_co_argcount')
#print(fn.__code__.co_argcount)

#print('get_code_object_co_varnames')
#print(fn.__code__.co_varnames)

#print('get_code_object_co_code')
#print(fn.__code__.co_code)

#print('get_code_object_co_consts')
#print(fn.__code__.co_consts)

#print('get_code_object_co_cellvars')
