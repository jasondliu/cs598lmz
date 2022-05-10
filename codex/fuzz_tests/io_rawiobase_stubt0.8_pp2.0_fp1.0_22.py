import io
class File(io.RawIOBase):
    '''A wrapper class for file-like objects.'''

    def __init__(self, file):
        self.file = file
        self.seekable = getattr(file, 'seekable', None)()

    def readable(self):
        return True

    def writable(self):
        return True

class Executor:
    '''The executor for a given sandbox.

    A sandbox is uniquely identified by a given sandbox_path. An executor
    can be constructed for a given sandbox by calling get_executor(sandbox_path).
    Calling that method is preferred over creating an executor directly.
    '''

    def __init__(self, sandbox_path):
        self.sandbox_path = sandbox_path
        self.process = None
        self.stdin = None
        self.stdout = None
        self.stderr = None
        self.current_command = ''

    @staticmethod
    def get_executor(sandbox_path):
        '''Get the executor for a given sandbox.'''
        executor = Executor(sandbox
