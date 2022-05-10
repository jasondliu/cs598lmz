import types
types.SimpleNamespace = types.SimpleNamespace


def map_dtype(dtype):
    """
    Map numpy datatype to python3 types module.
    
    Parameters
    ----------
    dtype: numpy.dtype
        
    Returns
    -------
    type
    """
    if np.issubdtype(dtype, np.integer):
        return types.Integer
    if np.issubdtype(dtype, np.floating):
        return types.Float
    if np.issubdtype(dtype, np.bool_):
        return types.Boolean
    if np.issubdtype(dtype, np.str_):
        return types.String


# https://github.com/flask-restplus/flask-restplus/issues/72
def parse_docstring(docstring):
    """
    Parse the  first paragraph of a docstring.
    
    Parameters
    ----------
    docstring: str
    
    Returns
    -------
    str:
    """
    if not docstring:
       
