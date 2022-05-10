import mmap
import re
import os
import os.path

from .. import config

class Importer(object):

    def __init__(self):
        pass

    def __call__(self):
        self.import_all()
