import types
types.ClassType
def is_class(obj):
    """
    Based on http://stackoverflow.com/a/11752464/430364
    """
    return obj.__class__.__name__ == 'classobj'

class StandardErrorMock(object):
    def __init__(self, name, err_msg):
        self.name = name
        self.err_msg = err_msg
    def __repr__(self):
        return '{}({})'.format(self.name, self.err_msg)

class StandardError(Exception):
    pass

def mock_std_error(name, err_msg):
    if name == 'KeyboardInterrupt':
        raise KeyboardInterrupt
    raise StandardError(StandardErrorMock(name, err_msg))
