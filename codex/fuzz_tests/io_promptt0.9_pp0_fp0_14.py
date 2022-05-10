import io
# Test io.RawIOBase and io.BufferedIOBase inherit from IOBase
issubclass(io.RawIOBase, io.IOBase)
issubclass(io.BufferedIOBase, io.IOBase)
# Verify Flushable and Seekable are included
issubclass(io.RawIOBase, io.Flushable)
issubclass(io.BufferedIOBase, io.Flushable)

issubclass(io.RawIOBase, io.Seekable)
issubclass(io.BufferedIOBase, io.Seekable)
# Verify the new stream types are included under RawIOBase and BufferedIOBase
from io import RawIOBase as rb, BufferedIOBase as bb

issubclass(io.FileIO, rb)
issubclass(io.BytesIO, rb)
issubclass(io.BufferedReader, bb)
issubclass(io.BufferedRandom, bb)
issubclass(io.BufferedWriter, bb)
# Verify the new stream types are included under IOBase
from io import IOBase as b


