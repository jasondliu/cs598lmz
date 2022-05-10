import weakref

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QWidget, QApplication

from . import mainwindow_rc
from .ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget, Ui_MainWindow):
    """Main window of the application."""

    # Signal emitted when the user wants to create a new project.
    newProject = pyqtSignal()

    # Signal emitted when the user wants to open a project.
    openProject = pyqtSignal()

    # Signal emitted when the user wants to save the current project.
    saveProject = pyqtSignal()

    # Signal emitted when the user wants to save the current project under a new name.
    saveAsProject = pyqtSignal()

    # Signal emitted when the user wants to close the current project.
    closeProject = pyqtSignal()

    # Signal emitted when the user wants to exit the application.
    exitApplication = pyqtSignal()

    # Signal emitted when the user wants to create a new document.
    new
