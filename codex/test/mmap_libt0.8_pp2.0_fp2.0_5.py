import mmap
import re
import sys

from typing import Tuple, Optional


def find_next_file(line: str) -> Tuple[str, Optional[str]]:
    """
    Returns (name, [next])
    where
    * name is the name of the next file that is about to be open
    * next is the index of the next file opened, if any.

    >>> find_next_file('  File "../../../../../../../../../lib/python3.7/pdb.py", line 1658, in main')
    ('pdb.py', '1658')
    >>> find_next_file('  File "<frozen importlib._bootstrap>", line 210, in _call_with_frames_removed')
    ('importlib._bootstrap', '210')
    """
    #  File "<frozen importlib._bootstrap>", line 1283, in _find_and_load_unlocked
    m = re.match(r'  File "\.{2,}/([^,]+)"', line)
