import weakref

from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

from . import log
from . import model
from . import util
from . import view

logger = log.get_logger(__name__)


class Controller(QObject):
    """
    The main controller object.
    """

    # Signals

    #: Emitted when a new model is loaded.
    model_changed = pyqtSignal(object)

    #: Emitted when the model is changed.
    model_updated = pyqtSignal(object)

    #: Emitted when the current view is changed.
    view_changed = pyqtSignal(object)

    #: Emitted when the current view is updated.
    view_updated = pyqtSignal(object)

    #: Emitted when the current view is updated.
    view_updated_at_timestamp = pyqtSignal(object, float)

    #: Emitted when the current view is updated.
    view_updated_at_timepoint = pyqtSignal(object, int)
