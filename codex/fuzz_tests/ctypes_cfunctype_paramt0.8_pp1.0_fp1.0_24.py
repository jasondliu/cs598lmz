import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)

# export the function to ctypes
# args: function to export,
# args: function type,
# args: function name,
# args: function docstring

module.add_function(cos, FUNTYPE, "cos", "Cosine")

# compile the generated code
module.compile()


# in python
from cos_module import cos
cos(0.1)
# 0.9950041652780258
cos(0.2)
# 0.9800665778412416
cos(0.3)
# 0.960170286650366
cos(0.4)
# 0.9320390859672264
cos(0.5)
# 0.8775825618903728
cos(0.6)
# 0.8090169943749475
cos(0.7)
# 0.7289686274214115
cos(0.8)
# 0.6427876096865393
cos(0.9)
# 0.54030230
