import weakref
import os
import sys
import re
import collections

from .libcli.cli import CLI
from .libcli.ui.label import CLILabel
from .libcli.ui.edit import CLIEdit
from .libcli.ui.scroll import CLIScroll
from .libcli.ui.status import CLIStatus
from .libcli.ui.dialog import CLIDialog
from .libcli.ui.dialog.yesno import CLIYesNo
from .libcli.ui.dialog.messagebox import CLIMessageBox
from .libcli.ui.dialog.errorbox import CLIErrorBox
from .libcli.ui.dialog.progressbar import CLIProgressBar
from .libcli.ui.dialog.inputbox import CLIInputBox
from .libcli.ui.dialog.filebrowser import CLIFileBrowser
from .libcli.ui.dialog.filebrowser import CLIFileBrowserDialog
from .libcli.ui.dialog.menubar import CLIMenuBar
