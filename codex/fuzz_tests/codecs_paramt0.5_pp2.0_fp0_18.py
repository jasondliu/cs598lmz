import codecs
codecs.register_error('strict', codecs.ignore_errors)

# ------------------------------------------------------------------------------

def list_files(root, ext=None, abspath=False, recursive=False):
    '''
    List all files in the given directory.

    :param root: the root directory to start from
    :param ext: a list of extensions to filter the files by
    :param abspath: return absolute paths or paths relative to the root
    :param recursive: if True, list all files in subdirectories as well
    :return: a list of file paths
    '''

    if ext is not None:
        if isinstance(ext, str):
            ext = [ext]
        ext = [e.lower() for e in ext]
    if not abspath:
        root = os.path.abspath(root)
    if recursive:
        files = []
        for dirpath, dirnames, filenames in os.walk(root):
            for filename in filenames:
                if ext is None or os.path.splitext(filename)[1].lower() in ext:
                    if abspath:

