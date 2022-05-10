import types
types.MethodType(my_method, my_object)

# or

my_object.my_method = my_method

# or

from types import MethodType
my_object.my_method = MethodType(my_method, my_object)
</code>

