import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double)

# wrapper functions should be static
@staticmethod
def isOption():
    return True

@staticmethod
def getType():
    return EUOptionType.Call

@staticmethod
def getPricingDate():
    return "2019-11-19"

@staticmethod
def getStrikePrice():
    return 1000.0

@staticmethod
def getExpiryDate():
    return "2019-12-19"

@staticmethod
def getUnderlyingPrice():
    return 2000.0

@staticmethod
def getYieldRate():
    return 0.06

@staticmethod
def getVolatility():
    return 0.2

@staticmethod
def getInitialPremium():
    return 1800.0

#@staticmethod
def getStrikePrice(self):
    return 1000.0

# Bind all the functions to Python
my_module.isOption.restype = ctypes.c_bool
my_module.isOption.argtype = FUNTYPE
# my_module.getType = my_module.getType
my
