import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from PyInstaller.utils.win32.winutils import winutils


def test_get_special_folder_path():
    """
    Test function PyInstaller.utils.win32.winutils.get_special_folder_path().
    """
    # Get Windows Start Menu folder.
    path = winutils.get_special_folder_path(winutils.CSIDL_START_MENU)
    assert os.path.isdir(path)


def test_get_folder_paths():
    """
    Test function PyInstaller.utils.win32.winutils.get_folder_paths().
    """
    # Get Windows Start Menu folder.
    path = winutils.get_special_folder_path(winutils.CSIDL_START_MENU)
    folder_paths = winutils.get_folder_paths(path)
    # There should be folder with All Users and Current User.
    assert len(folder_paths) == 2
    assert '
