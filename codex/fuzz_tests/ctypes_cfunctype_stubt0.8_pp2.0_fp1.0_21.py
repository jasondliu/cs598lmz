import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    raise NotImplemented()

class MyError(StandardError):
    pass

class Grid:
    """
    A tiling of the plane by squares.

    A grid is a tiling of the plane into squares.
    The squares can be of different sizes.

    Attributes:
        squares: a list of the squares in the grid.
        size: the number of rows and columns in the grid.

    """

    # A private class attribute.
    __square_id = 0

    def __init__(self, squares):
        """
        Set the list of squares for the grid.
        """
        self.squares = squares
        self.size = (len(squares), len(squares[0]))

    def __str__(self):
        """
        Return a string representation of the grid.
        """
        lines = ['-' * self.size[0] * 5]
        for row in self.squares:
            line = ''
            for sq in row:
                line += str(sq)
            line += '\n'
            lines.append(line)
