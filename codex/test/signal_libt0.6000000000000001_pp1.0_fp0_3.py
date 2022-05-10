import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk

from ubuntutweak.gui.gtk import set_busy, unset_busy
from ubuntutweak.gui.dialogs import ErrorDialog, InfoDialog, WarningDialog
from ubuntutweak.gui.dialogs import QuestionDialog, QuestionDialog2
from ubuntutweak.policykit.dbusproxy import proxy

from ubuntutweak.utils import icon
from ubuntutweak.common.debug import run_traceback

from ubuntutweak.modules  import TweakModule
from ubuntutweak.utils.i18n import _

class BaseDialog(Gtk.Dialog):
    '''BaseDialog is a dialog which has a title, a description, and a button.

    It's used for the first time user guide and some other dialogs
    '''
