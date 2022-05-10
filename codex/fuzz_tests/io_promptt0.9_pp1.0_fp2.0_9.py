import io
# Test io.RawIOBase and io.BufferedIOBase.

import io
import unittest

def _checkio(reader, reader_kwargs, writer, writer_kwargs, bufsize=None):
    if bufsize is not None:
        if writer is io.FileIO:
            # SF #1119426: on Windows, opening files in append mode and
            # with a non-zero buffer size is not supported.
            if 'mode' not in writer_kwargs and 'm' not in writer_kwargs:
                writer_kwargs = writer_kwargs.copy()
                writer_kwargs['mode'] = 'w+'
        elif 'buffering' not in reader_kwargs and 'buffering' not in writer_kwargs:
            reader_kwargs = reader_kwargs.copy()
            reader_kwargs['buffering'] = bufsize
            writer_kwargs = writer_kwargs.copy()
            writer_kwargs['buffering'] = bufsize
    r = reader(**reader_kwargs)
    w = writer(**writer_kwargs)
    w.seek(
