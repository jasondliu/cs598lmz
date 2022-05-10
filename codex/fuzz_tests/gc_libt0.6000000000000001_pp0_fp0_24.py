import gc, weakref, collections

#--------------------------------------------------------------------------------
#   Helper functions
#--------------------------------------------------------------------------------

def is_string(s):
    return isinstance(s, str) or isinstance(s, unicode)

def is_string_like(s):
    return hasattr(s, 'lower')

def is_list_of_strings(l):
    return all(is_string(i) for i in l)

def is_list_of_string_like(l):
    return all(is_string_like(i) for i in l)

def is_list_of_collections(l):
    return all(isinstance(i, collections.Collection) for i in l)

def is_list_of_collections_of_strings(l):
    return all(is_list_of_strings(i) for i in l)

def is_list_of_collections_of_string_like(l):
    return all(is_list_of_string_like(i) for i in l)

def str2list(s):
    if is
