import types
types.ModuleType
#/def


#------------------------------------------------------------------------------
def load(dotted_name):
    """
    Load the module with python dotted name.
    Shift anything to the string.__mod__
    Use it to hold all in one place.
    """
    if isinstance(dotted_name, (tuple, list)):
        dotted_name = ".".join(dotted_name)

    if not isinstance(dotted_name, StringTypes):
        dotted_name = str(dotted_name)

    if ":" in dotted_name:
        dotted_name = dotted_name.split(":")[0]

    if not dotted_name:
        raise ValueError("Empty module name.")

    return import_module(dotted_name)
#/def

#------------------------------------------------------------------------------
def check(dotted_name):
    """
    Same as load(...), but return (True, module) if loaded
    or (False, None) otherwise.

    Used in load or fail cases.
    """
