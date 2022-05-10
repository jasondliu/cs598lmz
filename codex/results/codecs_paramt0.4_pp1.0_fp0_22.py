import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_files(path, ext):
    return [f for f in os.listdir(path) if f.endswith(ext)]

def _get_files_recursive(path, ext):
    files = []
    for f in os.listdir(path):
        if f.endswith(ext):
            files.append(os.path.join(path, f))
        elif os.path.isdir(os.path.join(path, f)):
            files.extend(_get_files_recursive(os.path.join(path, f), ext))
    return files

def _get_files_recursive_with_path(path, ext):
    files = []
    for f in os.listdir(path):
        if f.endswith(ext):
            files.append(os.path.join(path, f))
        elif os.path.isdir(os.path.join(path, f)):
            files.extend(_get_files_recursive
