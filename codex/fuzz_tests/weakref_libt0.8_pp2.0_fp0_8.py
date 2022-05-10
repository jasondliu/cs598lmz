import weakref
import PySide.QtGui as QtGui
import PySide.QtCore as QtCore


class HistoryView(QtGui.QWidget):
    ''' Widget containing a list of previously opened files and project folders.

    '''

    def __init__(self, parent=None):
        ''' Initialize HistoryView.

        Parameters
        ----------
        parent : QtGui.QWidget
            Parent widget.

        '''
        super(HistoryView, self).__init__(parent)
        self.history = []
        self.selected = None
        self.models = weakref.WeakKeyDictionary()

        self.view = QtGui.QListView(self)
        self.view.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.view.selectionModel().selectionChanged.connect(self._on_selection_changed)
        self.view.pressed.connect(self._on_item_pressed)

        self.clear_button = QtGui.QPushButton('Clear History', self)
        self
