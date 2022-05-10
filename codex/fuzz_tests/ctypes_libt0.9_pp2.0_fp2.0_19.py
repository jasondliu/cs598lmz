import ctypes
ctypes.cdll.LoadLibrary('./csl.so')

@oacore
def get_d_names_c(shape_tuple, d_arr):
    '''get d_names of a d_array

    Parameters
    ----------
    shape_tuple : tuple of ints
        The shape of the array
    d_arr : np.ndarray
        The array itself

    Returns
    -------
    names, types : tuple of tuple of strings and tuple of strings
        The d_names and d_types of the array.
        The names and types tuples are of the same length.
    '''
    [names, types] = csl_proc.get_d_names(shape_tuple, d_arr)
    return names, types

@oacore
def has_d_names_c(shape_tuple, d_arr):
    '''check if a d_array has d_names

    Parameters
    ----------
    shape_tuple : tuple of ints
        The shape of the array
    d_arr : np.ndarray
        The
