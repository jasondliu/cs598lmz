import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

#
#
#

def get_all_files(path, ext=None):
    """
    Returns a list of all files in a directory, recursively.

    :param path: The path to the directory.
    :param ext: The extension of the files to be returned.
    :return: A list of all files in the directory.
    """
    if ext is not None:
        if not ext.startswith('.'):
            ext = '.' + ext
    files = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            if ext is None or f.endswith(ext):
                files.append(os.path.join(path, f))
        else:
            files.extend(get_all_files(os.path.join(path, f), ext))
    return files

#
#
#

