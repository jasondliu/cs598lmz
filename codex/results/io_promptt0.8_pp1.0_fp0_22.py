import io
# Test io.RawIOBase
from io import RawIOBase
# Test io.BufferedIOBase
from io import BufferedIOBase
# Test io.TextIOBase
from io import TextIOBase

# Test io.FileIO
from io import FileIO, BufferedReader, BufferedWriter
# Test io.BytesIO
from io import BytesIO

# Test io.StringIO
from io import StringIO

# Test io.TextIOWrapper
from io import TextIOWrapper
# Test io.BufferedReader
from io import BufferedReader
# Test io.BufferedWriter
from io import BufferedWriter
# Test io.BufferedRWPair
from io import BufferedRWPair

# Test io.BufferedRandom
from io import BufferedRandom

# Test io.BufferedRandom as a subclass
class X(BufferedRandom): pass

# Test io.FileIO as a subclass
class X(FileIO): pass

# Test io.BytesIO as a subclass
class X(BytesIO): pass

# Test io.StringIO as a subclass
class X(StringIO): pass

#
