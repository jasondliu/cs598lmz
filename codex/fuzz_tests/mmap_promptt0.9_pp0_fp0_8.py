import mmap
# Test mmap.mmap(0, size, access=mmap.ACCESS_COPY) before trying anything else
# EnvironmentError: [Errno 26] Text file busy: 'TestFile.txt'
# mmap.mmap(0, size, access=mmap.ACCESS_WRITE) also cause problems

# mmap example from https://docs.python.org/2/library/mmap.html

# Constants and variables required to manipulate the glyph dictionary
KEY_VALUE_SEPARATOR = '\t'

FONT_LIST_FILENAME = '/home/fonz/Fonts/FontList.txt'
GLYPH_LIST_FILEPATH = '/home/fonz/Fonts/glyphList.txt'
GLYPH_DICT_FILEPATH = '/home/fonz/Fonts/glyphDict.txt'

# Lines from fontlist.txt start with ., # or a-z,A-Z
fontListLineRE = re.compile(r'^[a-zA-Z0-9]|\..|\#')
# line from glyphList.
