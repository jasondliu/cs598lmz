import weakref


class FileLoader(Thread):
    """
    Loads the file in the background.
    """

    def __init__(self, path, parent=None):
        super(FileLoader, self).__init__()
        self.parent = weakref.proxy(parent)
        self.path = path
        self.daemon = True

    def run(self):
        # print("Loading {}".format(self.path))
        self.parent.new_file(self.path)


def ask_for_path():
    """
    Asks user for a path.
    """
    default = str(PyQt5.QtCore.QDir.homePath())
    title = "Open file"
    path, _ = PyQt5.QtWidgets.QFileDialog.getOpenFileName(None, title, default)
    return path

class Viewer:
    """
    Handles overall user interaction.

    Parameters
    ----------
    width : int, optional

    height : int, optional

    """

