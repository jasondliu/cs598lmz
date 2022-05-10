import lzma
lzma_codes = (lzma.FILTER_LZMA1, lzma.FILTER_DELTA)


class Dump(object):
    """Dumps a time and distance specific travel time graph to file.

    A temporary file is used to ensure that the compressed file is valid even
    if the program fails before completion (such as when the computer runs out
    of RAM).
    """

    def __init__(self, ttg):
        """Create a new dump instance.

        Parameters::
            ttg: TTG
                The time and distance specific travel time graph that should be
                dumped to file.
        """
        self.ttg = ttg
        self.files = {}
        self.num_records_written = 0

