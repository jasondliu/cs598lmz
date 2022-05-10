import weakref

class Widget(object):
    """
    Base class for all wxwidgets
    """

    def __init__(self, engine, parent, name, color, size, pos=None,
                 automap=True):
        """
        Create a Widget instance

        The Widget base class represents an elments of a patch. The Pyo
        stream is passed to the StreamPlayer object and a user interface
        is created with wxpython. This class defines the common methods
        for all widgets. The constructor only needs to be called by the
        subclasses.

        Parameters:

        engine : AudioEngine
            The AudioEngine global object.

        parent : wxFrame or wxDialog
            The widget parent.

        name : string
            Name of the widget as in the PyoObject.

        color : tuple, list or string
            Color of the widget as RGB values.

        size : tuple or list
            Size of the widget in (width, height).

        pos : tuple or list, optional
            Position of the widget in the parent. Defaults to (0, 0).

        automap : boolean
