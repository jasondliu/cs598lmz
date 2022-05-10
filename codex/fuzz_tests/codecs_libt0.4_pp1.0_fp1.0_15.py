import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from mainwindow import Ui_MainWindow
from new_project import Ui_NewProjectDialog
from new_file import Ui_NewFileDialog
from new_folder import Ui_NewFolderDialog
from new_url import Ui_NewUrlDialog
from new_text import Ui_NewTextDialog
from new_markdown import Ui_NewMarkdownDialog
from new_html import Ui_NewHtmlDialog
from new_css import Ui_NewCssDialog
from new_js import Ui_NewJsDialog
from new_php import Ui_NewPhpDialog
from new_python import Ui_NewPythonDialog
from new_ruby import Ui_NewRubyDialog
from new_c import Ui_NewCDialog
from new_cpp import Ui
