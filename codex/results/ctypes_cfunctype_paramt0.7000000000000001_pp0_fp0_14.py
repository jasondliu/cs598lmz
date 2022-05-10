import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)

# import our module and get the function
import randomgen as rg

# function
func = rg.get_random_int

# create the wrapper
wrapper = FUNTYPE(func)

# call the wrapper
print(wrapper())
print(wrapper())
print(wrapper())

# set the seed
rg.set_seed(0)

# call the wrapper
print(wrapper())
print(wrapper())
print(wrapper())
</code>

