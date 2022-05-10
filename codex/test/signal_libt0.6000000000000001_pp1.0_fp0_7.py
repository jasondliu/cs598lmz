import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

from .view import View
from .model import Model
from .controller import Controller


class Application(QApplication):
    """A class representing the application.

    Attributes
    ----------
    view : View
        The view of the application.
    model : Model
        The model of the application.
    controller : Controller
        The controller of the application.

    Methods
    -------
    on_timer()
        Updates the model and the view.
    """

    def __init__(self):
        """Constructs an application.

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        super(Application, self).__init__(sys.argv)
        self.view = View()
        self.model = Model()
        self.controller = Controller(self.model, self.view)
        self.view.show()

        # Update the
