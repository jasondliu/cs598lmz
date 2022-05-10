gi = (i for i in ())
# Test gi.gi_code (unbound built-in method)
check_attributes(gi.gi_code, 'co_argcount', 'co_names', 'co_varnames')

# Test sys.stdout
check_attributes(sys.stdout, 'name', 'mode', 'closed')

# Test sys.stdout.write
check_attributes(sys.stdout.write, '__self__', '__func__', '__code__')

# Test sys.getrefcount
check_attributes(sys.getrefcount, '__code__')

# Test _pickle.Pickler.dump
check_attributes(_pickle.Pickler().dump, '__self__', '__func__', '__code__')

# Test _struct.pack
check_attributes(_struct.pack, '__self__', '__func__', '__code__')

# Test _imp.create_dynamic
check_attributes(_imp.create_dynamic, '__self__', '__func__', '__code__')

# Test _functools.partial
check
