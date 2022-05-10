import codecs
codecs.register_error('tolerance', codecs.ignore_errors)


class PatchedFileVFS(object):
    """VFS that also supports saving files."""

    def __init__(self, vfs):
        self.vfs = vfs

    def __getattr__(self, name):
        return getattr(self.vfs, name)

    def open(self, path, mode='r'):
        mode = mode.replace('r', 'r').replace('w', 'w+')
        return self.vfs.open(path, mode)

    def save_file(self, path, content):
        with self.open(path, "w+") as f:
            f.write(content)
            return True

    def join(self, *args):
        if args[0] == "":
            args = args[1:]
        return self.vfs.join(*args)


class PatchedApp(WSGIApplication):
    """Monkey patch WSGIApplication so we can access the VFS."""

    def __init__(self, *args, **
