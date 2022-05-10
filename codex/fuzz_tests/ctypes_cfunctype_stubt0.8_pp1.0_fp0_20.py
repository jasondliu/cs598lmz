import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ("spam")

logging.basicConfig(format='%(levelname)s:%(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)

class Pipe(object):
    """The Pipe object represents a running pipe to an external program.

    Parameters
    ----------
    command : str
        The command to run using an external program.
    stdout : str, optional
        Used to redirect stdout to a file.
    stderr : str, optional
        Used to redirect stderr to a file.
    """
    def __init__(self, command, stdout=None, stderr=None):
        self.command = command.split(' ')
        self.process = None
        if stdout is not None:
            self.outfile = open(stdout, 'w')
        if stderr is not None:
            self.errfile = open(stderr, 'w')
        self.logger = logging.getLogger(__name__)
        self
