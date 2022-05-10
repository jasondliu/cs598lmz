from _struct import Struct
s = Struct.__new__(Struct)
s.size = lambda: 1
s.pack = lambda *args: b'\x01'

class TemporaryDirectory(object):
    def __init__(self, suffix='', prefix='tmp', dir=None):
        if dir is None:
            dir = os.environ['TMPDIR']
        self.name = tempfile.mkdtemp(suffix, prefix, dir)

    def cleanup(self):
        rmtree(self.name)

_tempdir_registry = []
def register_tempdir(dir):
    _tempdir_registry.append(dir)
def cleanup_tempdirs():
    for dir in _tempdir_registry:
        dir.cleanup()

def assert_raises(expected_exception, function, *args, **kwargs):
    try:
        function(*args, **kwargs)
    except expected_exception:
        pass
    except:
        raise AssertionError("%r was not raised" % expected_exception)
    else:
        raise AssertionError("%r was not raised
