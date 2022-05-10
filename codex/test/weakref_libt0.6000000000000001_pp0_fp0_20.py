import weakref

from . import _cvsgui_globals, _common, _config, _cvswidget, _error, _helpers, _i18n, _rcs, _scm, _vc, _widgets
from . import _widgets


class CommitDialog(object):
    """
    This class displays a dialog box asking the user to enter a log message
    and select which files to commit.
    """

    def __init__(self, files, parent=None):
        """
        Initialize the class.

        @param files: a list of files to be committed
        @type files: list

        @param parent: the parent window
        @type parent: L{wx.Window}
        """
        self.__files = files
        self.__parent = parent

        # Create the dialog
