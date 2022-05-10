from bz2 import BZ2Decompressor
BZ2Decompressor.flush = lambda self: b""


class TemporaryDirectory(object):
    """Context manager for bidning a temporary directory.

    This class implements the context manager protocol and provides a safe
    interface to the class CLIRunner.

    Attributes:
        path (str): The path of the temporary directory.
    """

    def __init__(self):
        self._path = None

    def __enter__(self):
        """Creates the temporary directory.

        Returns:
            TemporaryDirectory: The context manager instance.
        """
        self._path = tempfile.mkdtemp()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Deletes the temporary directory."""
        shutil.rmtree(self._path, ignore_errors=True)

    @property
    def path(self):
        return self._path


class CLIOutputParser(object):
    """Base class for parsing the standard output of the CLI command.

    Attributes:
        has_stdout (bool): Whether the specified CLI command wrote something
            to the standard output.

