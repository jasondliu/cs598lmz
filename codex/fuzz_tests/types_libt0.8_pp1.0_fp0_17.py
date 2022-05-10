import types
types.InstanceType = type

from inspect import getmembers

def print_signatures(cls_to_inspect, input_text = '', print_doc = True):
    '''Prints all methods, constructors, and static methods in a class'''
    def print_sig(method):
        print "%s(%s)" % (method[0], method[1].__doc__)

    def print_methods(methods, input_text = ''):
        print input_text
        map(lambda m: print_sig(m), methods)
        print

    print "\n".join(cls_to_inspect.__doc__.split('\n')[1:-1])
    print_methods(filter(lambda x: x[0] == '__init__', getmembers(cls_to_inspect)), "Constructors:")
    print_methods(filter(lambda x: type(getattr(cls_to_inspect, x[0])) == types.MethodType and x[0][0] != '_', getmembers(cls_to
