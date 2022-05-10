import _struct
import linkedList

def _convertToSparse(matrix):
    """Convert to sparse matrix format from any type of input:
    None - no matrix at all.
    
    List or tuple of tuples.
    
    Matrix (as defined previously).
    
    """
    
    extraLists = False
    if isinstance(matrix, (list, tuple)):
        if len(matrix) == 0: # Empty tuple or list
            matrix = _struct.Matrix()
        elif matrix[0] == None: # Only None values
            matrix = _struct.Matrix(rowCount=len(matrix), colCount=1)
        elif isinstance(matrix[0], _struct.Matrix): # Multiple matrices
            extraLists = True
        elif isinstance(matrix[0], (list, tuple)): # Matrix represented as list or tuple of lists or tuples
            # A list or tuple of lists or tuples is modified differently than a matrix
            if isinstance(matrix[0][0], _struct.Matrix):
                extraLists = True

