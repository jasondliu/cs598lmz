import mmap
import os
import re
import subprocess
import sys
import time

from lib.cuckoo.common.abstracts import Processing
from lib.cuckoo.common.config import Config
from lib.cuckoo.common.constants import CUCKOO_ROOT
from lib.cuckoo.common.exceptions import CuckooProcessingError
from lib.cuckoo.common.objects import File
from lib.cuckoo.common.utils import convert_to_printable
from lib.cuckoo.core.database import Database

# Global variables.
config = Config()
db = Database()

class Strings(Processing):
    """Extracts strings from the analyzed file."""

    def run(self):
        """Run extract of printable strings.
        @return: list of printable strings.
        """
        self.key = "strings"
        strings = []

        if not os.path.exists(self.file_path):
            raise CuckooProcessingError("Sample file doesn't exist: \"%s\"" % self.file_path)
