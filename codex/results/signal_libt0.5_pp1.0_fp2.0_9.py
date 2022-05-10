import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from qutepart import Qutepart
from qutepart.contrib.completer import Completer
from qutepart.contrib.completer import CodeCompletionModel
from qutepart.contrib.completer import HtmlCompletionModel
from qutepart.contrib.completer import FileSystemCompletionModel
from qutepart.contrib.completer import ShellCompletionModel
from qutepart.contrib.completer import LanguageCompletionModel
from qutepart.contrib.completer import PythonCompletionModel
from qutepart.contrib.completer import PythonFunctionDoc
from qutepart.contrib.completer import PythonModuleDoc
from qutepart.contrib.completer import PythonClassDoc
from qutepart.contrib.completer import PythonCompletion
