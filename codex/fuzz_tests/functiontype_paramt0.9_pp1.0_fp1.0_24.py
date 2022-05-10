from types import FunctionType
list(FunctionType('id',lambda x:x,'id').__code__.co_consts)

# return an object representing a constant from a code object.
def consts(constants:list,values:list):
    return dict(zip([constant for constant in constants if not isinstance(constant,FunctionType)],values))

# return None if the argument is not a constant
def const(constant:object):
    if not isinstance(constant,FunctionType):
        return constant
    else:
        return None

# return True if the object is a constant
def is_const(constant:object):
    return isinstance(constant,int) or isinstance(constant,str)

# name of the node
def name(node:tuple):
    return node[0]

# return the type of the node
def node_type(node:tuple):
    return node[1]

# return a dict of the attributes
def kwargs(node:tuple):
    return node[2]

# return a list of the arguments
def args(node:tuple
