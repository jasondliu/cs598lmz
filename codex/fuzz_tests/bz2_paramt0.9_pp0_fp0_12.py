from bz2 import BZ2Decompressor
BZ2Decompressor

from common.file import Path

from fetch.copy import Copy
from fetch.parse import Parser
from fetch.raw import Raw
from fetch.result import Result
from fetch.version import WebSite


_raw = Raw()
_copy = Copy()
_parse = Parser()


class _Build:
    """The factory responsible for revising the file paths."""

    def __init__(self, patch: pathlib.PurePath) -> None:
        """Return a new object to be used within the class."""
        self._patch = patch

    def __call__(self, result: Result) -> pathlib.PurePath:
        """Return the name of the file with the directory path changed."""
        return self._patch.joinpath(result.name.relative_to(result.source))


def _fetch(uri: str, result: Result) -> Result:
    """
    Fetch the requested web page.

    In this method, the data is unarchived and structured before being passed
    to the parser.
    """
    start = Stopwatch.start()
    locations = _
