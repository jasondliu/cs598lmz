import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress

#region Read/Write

def get_reader(format, path, force=True):
    """
    Returns a reader object for the given file format and path.

    Parameters
    ----------
    format : str
        One of the supported formats: Valid values depend on the which
        `readers <index>`_ have been installed, but include 'treetime'.
    path : str
        The path to the file to be read.

    Returns
    -------
    reader
        A reader object that can be used to load data from the file.

    Raises
    ------
    UnknownFormatError
        If no reader can be found for the given file format.

    .. _index: readers.html
    """
    if format in reader_registry:
        return reader_registry[format](path, force)
    else:
        raise UnknownFormatError(format)


def get_writer(format, path, force=True):
    """
    Returns a writer object for the
