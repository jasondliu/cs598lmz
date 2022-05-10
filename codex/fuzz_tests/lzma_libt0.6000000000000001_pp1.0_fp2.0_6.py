import lzma
lzma.decompress

from xml.dom.minidom import parse, parseString

from lib.core.datatype import AttribDict
from lib.core.common import singleTimeWarnMessage
from lib.core.exception import SqlmapNoneDataException
from lib.core.settings import PYVERSION
from lib.core.settings import UNICODE_ENCODING
from lib.core.settings import GZIP_PAYLOAD_ENCODING

def initOptions(cmdLineOptions=None):
    """
    This function parses command line options and returns them as a
    dictionary.
    """

    if cmdLineOptions is None:
        cmdLineOptions = sys.argv[1:]

    if len(cmdLineOptions) == 0:
        errMsg = "missing option(s). "
        errMsg += "Type 'sqlmap.py -h' for basic or 'sqlmap.py -hh' for advanced help message"
        raise SqlmapSyntaxException, errMsg

    options = AttribDict()

    try:
        opts, _ = getopt
