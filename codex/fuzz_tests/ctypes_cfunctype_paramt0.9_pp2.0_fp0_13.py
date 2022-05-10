import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)


def reverse_dict(dikt):
    """
    Turn a dictionary's key-value pairs into value-key paires
    """

    new_dikt = {}
    for key in dikt:
        new_dikt[dikt[key]] = key

    return new_dikt

def reverse_string(string):
    """
    Reverse string
    """

    rev_string = ""
    for i in range(-1, -len(string)-1, -1):
        rev_string += string[i]

    return rev_string

def get_nth_ancestor(node, n):
    """
    Get the n-th ancestor of a node
    """

    def helper(node, n):
        if n == 0:
            return node.parent

        return helper(node.parent, n-1)

    if n == 0:
        return node
    else:
        return helper(node, n)
