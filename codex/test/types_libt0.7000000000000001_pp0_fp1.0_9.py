import types
types.SetType = set

def _rmtree(top):
    if type(top) is not str:
        raise TypeError('expected string, got %s type' % type(top))
    if _exists(top):
        _call(['/bin/rm', '-rf', top])

def _copytree(src, dst, symlinks=False, ignore=None):
    if type(src) is not str:
        raise TypeError('expected string, got %s type' % type(src))
    if type(dst) is not str:
        raise TypeError('expected string, got %s type' % type(dst))
    names = _listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    if not _exists(dst):
        _makedirs(dst)
        copied_files = []
    else:
        copied_files = _listdir(dst)

