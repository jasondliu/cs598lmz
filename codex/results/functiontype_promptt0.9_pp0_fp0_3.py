import types
# Test types.FunctionType (a function)
# Assign f a function called atom_name
f = atom_name

# Use {0} to insert the variable
print ("A function comes from a module by name:{0}".format (f))

# Is it type FunctionType?
if type(f) == types.FunctionType:
    print ("atom_name is a function.")

# Is it type FunctionType?
if type(f) == types.ModuleType:
    print ("atom_name is a module.")
