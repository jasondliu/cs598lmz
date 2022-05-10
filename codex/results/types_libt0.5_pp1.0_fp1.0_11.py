import types
types.FunctionType.__call__ = types.MethodType.__call__
types.FunctionType.__get__ = types.MethodType.__get__
types.FunctionType.__set__ = types.MethodType.__set__
types.FunctionType.__delete__ = types.MethodType.__delete__

# ------------------------------------------------------------------------------

class Data(object):
    """
    The Data class is a container for data that can be added to a
    :class:`~vtkplotter.Plotter` object.
    The data can be of several types like numpy arrays, vtk objects,
    dictionaries, pandas dataframes, etc.
    The :class:`~vtkplotter.Plotter` will then use the :meth:`show` method
    to visualize it.

    The following example shows how to create a :class:`~vtkplotter.Data` object
    and add it to a :class:`~vtkplotter.Plotter` object.

    .. code-block:: python

        from vtkplotter import Data, Plotter
        import numpy as np

       
