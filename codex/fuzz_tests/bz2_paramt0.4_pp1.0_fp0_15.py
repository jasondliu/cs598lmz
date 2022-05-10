from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = bz2_decompress_patched

def _get_all_files(path):
    """
    Returns all files in a given directory.
    """
    files = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
    return files

def _get_all_subdirs(path):
    """
    Returns all subdirectories in a given directory.
    """
    subdirs = []
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            subdirs.append(file)
    return subdirs

def _get_all_subdirs_recursive(path):
    """
    Returns all subdirectories in a given directory and its subdirectories.
    """
    subdirs = []
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(
