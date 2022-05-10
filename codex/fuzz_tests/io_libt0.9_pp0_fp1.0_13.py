import io

# Some parts are based on Daniel Himmelstrup Pedersen's code.

try:
    str = unicode
except NameError:
    pass
    
    
def create_matlab_table(*args):
    """Create a string that is compatible with tables in matlab.

    The input can be one or several lists, tuples or arrays. One table with
    or without headers can be created from these.

    The function takes as many  lists, tuples or arrays as input arguments.
    All input variables have to have the same length. A single list is
    interpreted as one column in the table. If more than one list are input
    the lists are interpreted as rows in the table.

    The inputs can either be separeted by commas (1D tables), or by spaces
    (2D tables).

    Inputs:
    --------
    A = [1,2,3,4]
    B = [1.1,1.2,1.3]
    C = ['foor','bar','somemoretext']
    (A, B)
    (C, A
