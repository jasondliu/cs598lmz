import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.py_object)
def iter_hash(t):
    f = FUNTYPE(hash)
    return [f(x) for x in t]

def print_diff_waste_time(t):
    print('铁子 :', diff_waste_time('铁子'))
    print('铁子 :', c_diff_waste_time('铁子'))

    print(t, '[].extend', diff_waste_time(t, 'extend'))
    print(t, '[].append', diff_waste_time(t, 'append'))
    print(t, 'for...append', diff_waste_time(t, 'forappend'))
    print(t, 'for...extend', diff_waste_time(t, 'forextend'))
    print(t, '+=', diff_waste_time(t, '+='))
    print(t, 'list(list)', diff_waste_time(t, 'list_list'))
