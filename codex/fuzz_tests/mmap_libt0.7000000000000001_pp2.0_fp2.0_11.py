import mmap
import re
from typing import Tuple
from typing import Union

from . import base
from . import util


class Grep(base.SearchEngine):
    """Search for patterns in files with grep.

    Arguments:
        extensions: File extensions to search for.
        patterns: Patterns to search for. Can be a list or a dictionary.
        return_results: Flag to enable/disable returning results.
        return_stats: Flag to enable/disable returning stats.
        is_case_sensitive: Flag to enable/disable case sensitivity.
        is_regex: Flag to enable/disable the use of regex.
        is_multiline: Flag to enable/disable multiline patterns.
        is_whole_words: Flag to enable/disable whole word matching.
        is_invert_match: Flag to enable/disable inverted matches.
        is_line_number: Flag to enable/disable line numbers.
        is_filename: Flag to enable/disable filenames.
    """

    def __init__(
        self,
        extensions: Union[str, List[str]] = None,
       
