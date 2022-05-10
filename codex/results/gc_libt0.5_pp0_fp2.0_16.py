import gc, weakref
from . import qt
from . import utils
from . import config

# from . import _version
# __version__ = _version.__version__
__version__ = '0.1.2'


class QTangoAttributeLabel(qt.QWidget):

    '''
    a QTangoAttributeLabel is a widget that displays the name, value and quality of a tango attribute.
    It is composed of:
      - a QLabel with the attribute name
      - a QLabel with the attribute value
      - a QLabel with the attribute quality
    '''

    def __init__(self, parent=None, designMode=False):
        qt.QWidget.__init__(self, parent)

        self.setWindowTitle('QTangoAttributeLabel')
        self.setObjectName('QTangoAttributeLabel')

        self.setLayout(qt.QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)

        self.nameLabel = qt.QLabel(self)
