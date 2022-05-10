import io
class File(io.RawIOBase):
    """
    A file-like object with block semantics.
    An instance can be created by passing a tuple, a list or a
    generator to the constructor:

        >>> samples = [b'block 1\\n', b'block 2\\n', b'block 3\\n']
        >>> f = File(samples)
        >>> f.read(2)
        b'bl'
        >>> f.read()
        b'ock 1\\nblock 2\\nblock 3\\n'

    A list of bytes can be passed to the constructor:

        >>> samples = [b'block 1\\n', b'block 2\\n', b'block 3\\n']
        >>> f = File(samples)
        >>> f.read()
        b'block 1\\nblock 2\\nblock 3\\n'

    A generator of bytes can be passed to the constructor:

        >>> import os
        >>> lines = [b'block 1\\n', b'block 2\\n', b'block 3\\n']
        >>> def create_block():
        ...     for line in lines:
        ...         yield line

