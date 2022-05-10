from types import FunctionType
list(FunctionType(add.__code__,globals()).__globals__.keys())[:5]

# add.__globals__
# add.__closure__

# add.__closure__[0]
# add.__closure__[0].cell_contents

# add.__closure__[1]
# add.__closure__[1].cell_contents

add(1,2)

# add.__globals__
# add.__globals__['add'] is add

# add.__globals__['add'](1,2)

add.__closure__

add.__closure__[0]
add.__closure__[0].cell_contents

add.__closure__[1]
add.__closure__[1].cell_contents

add.__closure__[0].cell_contents is add.__closure__[1].cell_contents

# def add(x,y):
#     return x+y

# add(1,2)

# add.__globals
