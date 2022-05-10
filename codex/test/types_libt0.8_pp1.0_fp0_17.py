import types
types.InstanceType = type

from inspect import getmembers

def print_signatures(cls_to_inspect, input_text = '', print_doc = True):
    '''Prints all methods, constructors, and static methods in a class'''
