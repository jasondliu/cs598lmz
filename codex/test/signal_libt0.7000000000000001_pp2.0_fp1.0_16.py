import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt

import sys
import os

from shared import Window
from shared import Constants
from shared.utils import Utils
from shared.utils import get_file
from shared.utils import get_file_content
from shared.utils import get_all_files_in_folder
from shared.utils import get_list_of_folders
from shared.utils import get_list_of_files
from shared.utils import print_file
