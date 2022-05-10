import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p)

#
# Call back into the Python short-circuit routines.
#


def short_circuit_py(key, value):
    """
    Short circuit the search_kv_cb() routine by
    returning a value.

    :param key: String key
    :param value: String value
    :return: Return the Python value
    """
    return (key, value)


def short_circuit_py_udata(udata, key, value):
    """
    Short circuit the search_kv_udata_cb() routine by
    returning a value.

    :param udata: User's data
    :param key: String key
    :param value: String value
    :return: Return the Python value
    """
    return (udata, key, value)


def short_circuit_py_udata_full(udata, key, value, idx):
    """
    Short circuit the search_kv_udata_cb() routine by
    returning a value.

    :param udata: User's
