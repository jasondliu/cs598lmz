import _struct
import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal

from . import resource
from . import const
from . import error
from . import languagetype

class BaseLanguage(ABC):
    def __init__(self, project_name):
        super(BaseLanguage, self).__init__()
        self.project_name = project_name
        self.languagetype = languagetype.LanguageType.NoneType
        self.widget = None
        self.window_title = ''
        self.file_list = []
        self.is_cancel = False

    @abstractmethod
    def check_project(self):
        pass

    @abstractmethod
    def get_file_list(self):
        pass

    @abstractmethod
    def get_file_content(self):
        pass

    def file_count(self):
        return len(self.file_list)

    def show_widget(self):
        if self.widget is None:

