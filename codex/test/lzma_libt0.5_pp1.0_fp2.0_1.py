import lzma
lzma.LZMAFile

def get_files(path):
    """
    Returns a list of files in the given path.
    """
    files = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path,f)):
            files.append(f)
    return files

def get_folders(path):
    """
    Returns a list of folders in the given path.
    """
    folders = []
    for f in os.listdir(path):
        if os.path.isdir(os.path.join(path,f)):
            folders.append(f)
    return folders

def get_file_size(file):
    """
    Returns the size of a file in bytes.
    """
    return os.path.getsize(file)

def get_folder_size(path):
    """
    Returns the size of a folder in bytes.
    """
    total_size = 0
