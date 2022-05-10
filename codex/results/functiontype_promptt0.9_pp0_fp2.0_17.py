import types
# Test types.FunctionType

def samplefunction(num):
    print "samplefunction"
    print "num=",num
    return

if isinstance(samplefunction,types.FunctionType):
    print "samplefunction is a function"
# Test types.ModuleType
import samplemodule
if isinstance(samplemodule,types.ModuleType):
    print "Module named samplemodule is a module"

# Test types.TypeType
a=2
if isinstance(a,types.TypeType):
    print "a is a type"
