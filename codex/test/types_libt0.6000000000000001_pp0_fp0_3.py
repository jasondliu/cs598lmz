import types
types.FunctionType = lambda x: 'function'

# This is a global variable and will be used by all the functions
global_count = 0

# This is a function that increments the global_count
def increment_global():
    global global_count
    global_count += 1

# This is a function that returns the global_count
def get_global_count():
    return global_count

# This is a function that increments the global_count using the global keyword
def increment_global_using_global():
    global global_count
    global_count += 1

# This is a function that increments the count variable in the closure
def increment_closure(count):
    count += 1
    return count

# This is a function that increments the count variable in the closure using the nonlocal keyword
