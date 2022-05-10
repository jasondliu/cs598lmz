import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyQt4 import QtGui
from gui.main_window import MainWindow
from gui.main_window.main_window_controller import MainWindowController
from gui.main_window.main_window_model import MainWindowModel


def main():
    """
    Entry point for the program.
    """
    app = QtGui.QApplication(sys.argv)

    # Create the main window model
    mw_model = MainWindowModel()

    # Load the settings
    mw_model.load_settings()

    # Create the main window controller
    mw_controller = MainWindowController()

    # Create the main window view
    mw_view = MainWindow()

    # Connect the model and the view
    mw_view.set_model(mw_model)
    mw_model.add_view(mw_view)

    # Connect the controller and the view
