import weakref

from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from plover.config import CONFIG_DIR
from plover.gui_qt.i18n import get_gettext
from plover.gui_qt.lookup_table_dialog import LookupTableDialog
from plover.gui_qt.utils import load_icon

_, _N = get_gettext()


class ConfigEditor(QWidget):

    def __init__(self, engine, config_spec, config, parent=None):
        super(ConfigEditor, self).__init__(parent=parent)
        self._engine = engine
        self._config_spec = config_spec
        self._config = weakref.proxy(config)
        self._lookup_table_dialog = LookupTableDialog(self)
        self._lookup_table_dialog.setWindowFlags(self.windowFlags()
                                                 | Qt.WindowStaysOnTopHint)
