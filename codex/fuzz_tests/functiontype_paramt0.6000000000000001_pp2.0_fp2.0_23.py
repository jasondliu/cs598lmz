from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# this is how you get a list of local variables in a function
def locals_list():
    x = 1
    y = 2
    z = 3
    return locals()

print(locals_list())

# this is how you get a list of global variables in a function
def globals_list():
    return globals()

print(globals_list())

# this is how you get a list of free variables in a function
def free_list():
    x = 1
    def free():
        y = 2
        print(locals())
        return globals()
    return free()

print(free_list())

# this is how you get a list of cell variables in a function
def cell_list():
    x = 1
    def cell():
        y = 2
        return locals()
    return cell()

print(cell_list())

# this is how you get a list of nonlocal variables in a function
def nonlocal_list():
    x = 1
   
