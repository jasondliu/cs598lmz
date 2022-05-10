import gc, weakref
from . import _util
from . import _props
from . import _widget
from . import _container

class Grid(_container.Container):
    """
    Grid widget.

    Args:
        id (str): An identifier for this widget.
        style (:py:class:`Style`): An optional style object. If no style is provided then a
            new one will be created for the widget.
        rows (int): The number of rows in the grid.
        columns (int): The number of columns in the grid.
        properties (dict): An optional dict of properties that will be set on
            the widget.
    """
    def __init__(self, id=None, style=None, rows=1, columns=1, properties=None):
        super(Grid, self).__init__(id=id, style=style, rows=rows, columns=columns, properties=properties)

    def _configure(self, rows, columns, properties):
        self._rows = rows
        self._columns = columns
        self._grid_widgets = [[None for j in range(
