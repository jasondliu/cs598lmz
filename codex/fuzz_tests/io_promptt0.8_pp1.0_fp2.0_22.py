import io
# Test io.RawIOBase for presence of read()
try:
    io.RawIOBase().read()
except AttributeError:
    # read not present, it must be python < 2.7
    from legacyio import legacy_input
else:
    from io import FileIO as legacy_input

# this import is ok.
from io import BlockingIOError
BlockingIOError

# xxx:
# - io.StringIO has no 'fileno' method
# - io.TextIOWrapper has no 'fileno' method
# - maybe we don't actually need to support the various text files?
# - what about other io classes?
# How to test:
# - ask stackoverflow? https://stackoverflow.com/questions/538950/how-should-i-test-python-code-that-emits-warnings
# - maybe ftp://selab.janelia.org/pub/publications/Margoliash-1966.pdf has hints?
# - text files should be open()'d as "r" or "w" or "rw"
# - binary files should be open()
