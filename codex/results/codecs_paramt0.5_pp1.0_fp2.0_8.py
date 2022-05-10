import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# Classes
#

class Logger(object):
    """
    A class that allows for logging to go to stdout and a file.
    """
    def __init__(self, log_file=None, verbosity=None):
        """
        Initializes the logger.

        @param log_file: The log file to write to.
        @type log_file: str
        @param verbosity: The verbosity level.
        @type verbosity: int
        """
        self.log_file = log_file
        self.verbosity = verbosity
        if self.log_file:
            self.log_file = codecs.open(self.log_file, 'a', encoding='utf-8',
                                        errors='strict')
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        sys.stdout = self
        sys.stderr = self

    def __del__(self):
        """
        Destructor.
        """
       
