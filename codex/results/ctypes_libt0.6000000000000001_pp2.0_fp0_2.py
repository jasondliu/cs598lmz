import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

def open_folder_in_explorer(path):
    path = os.path.realpath(path)
    os.startfile(path)

def new_folder_from_path(path):
    """
    :param path: str
    :return: str
    """
    base, filename = os.path.split(path)
    os.makedirs(os.path.join(base, filename))
    return os.path.join(base, filename)

def new_folder_from_name(name, path=None):
    """
    :param name: str
    :param path: str
    :return: str
    """
    if path is None:
        path = os.getcwd()
    os.makedirs(os.path.join(path, name))
    return os.path.join(path, name)

def get_file_list(path, extension=None, recursive=False):
    """
    :param path: str
    :
