import types
# Test types.FunctionType and types.LambdaType
F = types.FunctionType
L = types.LambdaType

# CPython 2 uses types.ClassType for classes
try:
    types.ClassType
except AttributeError:
    pass
else:
    O = types.ClassType # class object

# CPython 2 uses types.InstanceType for instances
try:
    types.InstanceType
except AttributeError:
    pass
else:
    I = types.InstanceType # instance object

rules = ttyRuleSet()
# Constants
rules.addOption("constant",highlight("yellow on black",Enum))
rules.common("constant",highlight("yellow on black",(type, types.ModuleType, types.BuiltinFunctionType, F, L)))

# Keywords
rules.addOption("keyword",highlight("cyan on black"))
rules.common("keyword",highlight("yellow on black", None))
# rules.common("keyword",highlight("cyan on black"))

rules.addOption("comment",highlight("default on black"))
rules.add
