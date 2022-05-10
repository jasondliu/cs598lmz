import mmap
import os
import re
import subprocess
import sys
import time

from lib.cuckoo.common.abstracts import Processing
from lib.cuckoo.common.exceptions import CuckooProcessingError
from lib.cuckoo.common.objects import File
from lib.cuckoo.common.utils import convert_to_printable, to_unicode

class Strings(Processing):
    """Extract printable strings from files."""

    def run(self):
        """Run extract of printable strings.
        @return: list of printable strings.
        """
        self.key = "strings"
        strings = []

        for file_path in self.file_paths:
            file_path = file_path.encode("ascii", errors="ignore")
            file_data = open(file_path, "rb").read()
            strings.append({"file": file_path, "strings": self.strings_extract(file_data)})

        return strings

    def strings_extract(self, data):
        """Extract print
