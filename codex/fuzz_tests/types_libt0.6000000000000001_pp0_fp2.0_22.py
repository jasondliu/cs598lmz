import types
types.SimpleNamespace

def make_id(prefix, suffix):
    """
    make a new id
    """
    return prefix + '_' + str(suffix) + '_id'

def make_id_with_param(prefix, suffix, param):
    """
    make a new id
    """
    return prefix + '_' + str(suffix) + '_id' + str(param)

def make_name(prefix, suffix):
    """
    make a new name
    """
    return prefix + '_' + str(suffix) + '_name'

def make_name_with_param(prefix, suffix, param):
    """
    make a new name
    """
    return prefix + '_' + str(suffix) + '_name' + str(param)

def make_name_with_param_and_id(prefix, suffix, param, id):
    """
    make a new name
    """
    return prefix + '_' + str(suffix) + '_name' + str(param) + str(
