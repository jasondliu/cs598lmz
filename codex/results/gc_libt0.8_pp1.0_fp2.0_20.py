import gc, weakref
import numpy as np
import matplotlib.pyplot as pp


class Surface:
    """A class for 3D surfaces.
    
    The class is instantiated by giving a function R(x,y) which is
    evaluated on a NxN grid to create a surface. It provides methods
    to translate, rotate, set material properties and save or plot the
    surface.
    
    The class uses lazy evaluation. Translation, rotation, setting
    material properties, saving or plotting creates a new surface.
    Only the first of these two surfaces is kept in memory. The grid
    points of the second surface are found by applying the operation
    to the grid points of the first surface. The second surface also
    contains a reference to the first one. The grid points of the
    second surface are found by applying the operation to the grid
    points of the first surface. The second surface also contains a
    reference to the first one. And thus, when the second surface is
    garbage collected, so too are the points of the first surface.
    
    A reference to a surface can be created by the function
    Surface.keep(sur
