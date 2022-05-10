import weakref

from plotutils import data_store
from plotutils import plot

from dialogs import text_input


class Spectra(QtGui.QTimeEdit):
    """
    A list of wavelengths used in the simulator.
    """
    def __init__(self, parent=None):
        super(Spectra, self).__init__(parent)
        self.parent = parent
        self.store = data_store.Store()
        self.block = False
        self.wavelengths = self.store.get_item('wavelengths')
        self.acts = [None,]
        self.menu = None
        self.resize(100, 50)
        self.update_view()
        self.setMaximumHeight(100)
        self.setAlignment(QtCore.Qt.AlignLeft)
        self.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.currentIndexChanged.connect(self.choose)

