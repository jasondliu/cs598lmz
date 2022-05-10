import codecs
codecs.register_error("strict", codecs.ignore_errors)

# from the Python docs
def walk(top, topdown=True, onerror=None):
    """Directory tree generator.
    https://docs.python.org/3.6/library/os.html#os.walk
    """
    names = os.listdir(top)
    dirs, nondirs = [], []
    for name in names:
        if os.path.isdir(os.path.join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)
    if topdown:
        yield top, dirs, nondirs
    for name in dirs:
        new_path = os.path.join(top, name)
        if os.path.islink(new_path):
            continue
        for x in walk(new_path, topdown, onerror):
            yield x
    if not topdown:
        yield top, dirs, nondirs

# from the Python docs
def copytree(src, dst, symlinks=False, ignore
