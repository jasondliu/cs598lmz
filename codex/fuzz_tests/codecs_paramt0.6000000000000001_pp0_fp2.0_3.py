import codecs
codecs.register_error('strict', codecs.ignore_errors)

import logging
logging.basicConfig(level=logging.DEBUG)

_log = logging.getLogger('data')

###############################################################################

class Data:
    """
    Data container.
    """

    def __init__(self, path):
        self.path = path
        self.data = []
        self.word_freq = {}
        self.word_index = {}
        self.class_freq = {}


    def load(self):
        """
        Load the data from the file.
        """
        self.data = []
        with open(self.path) as f:
            for line in f.readlines():
                line = line.strip()
                if len(line) == 0:
                    continue
                parts = line.split('\t')
                if len(parts) != 2:
                    raise Exception("Line should have two parts: '%s'" % line)
                _log.debug("%s %s", parts[0], parts[1])
                self.data
