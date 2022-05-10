import bz2
bz2_type = type(bz2.BZ2File(__file__, 'r'))
if bz2_type:

    class BZ2_TextIOWrapper(io.TextIOWrapper):
        """A TextIOWrapper for bz2 files.

        This class is identical to TextIOWrapper from the standard library,
        except the constructor takes a 'mode' argument instead of a 'buffering'
        argument.  See the docstrings for TextIOWrapper and BZ2File for
        more details.
        """

        def __init__(self, bz2_file, mode='r', encoding=None, errors=None,
                newline=None):
            """Create a wrapper for bz2 file.

            The wrapper implementation is different from the implementation in
            the stdlib: it takes a 'mode' option instead of 'buffering'.
            This is because bz2 always buffered the file.
            It's taken from bz2file.py from python 2.7.

            "bz2_file" should be an instance of bz2
