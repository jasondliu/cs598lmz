import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gtk

from kiwi.ui.dialogs import KiwiMessageDialog
from kiwi.ui.dialogs import KiwiEntryDialog
from kiwi.ui.dialogs import KiwiConfirmationDialog
from kiwi.ui.dialogs import KiwiErrorDialog

from kiwi.ui.widgets.combo import ProxyComboBoxEntry
from kiwi.ui.widgets.checkbutton import ProxyCheckButton
from kiwi.ui.widgets.radiobutton import ProxyRadioButton
from kiwi.ui.widgets.entry import ProxyEntry
from kiwi.ui.widgets.label import ProxyLabel
from kiwi.ui.widgets.button import ProxyButton
from kiwi.ui.widgets.textview import ProxyTextView
from kiwi.ui.widgets.togglebutton import ProxyToggleButton
from kiwi.ui.widgets.progressbar import ProxyProgressBar
from kiwi.ui.widgets.image import ProxyImage

