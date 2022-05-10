import io
class File(io.RawIOBase): pass
class NotImplementedError(Exception): pass

# Font type mappings
TEST = 0
BITMAP = 1
PICTURE = 2
SCREENFONT = 3

CDRIVER = 64
CREFCNT = 65
CSIZE = 66
CPEN = 67
CCOLOR = 68
CDEPTH = 69
CMODE = 70
CGRAFX = 71

PEN = 1
COLOR = 2
DEPTH = 4
MODE = 8
GRAFX = 16
XOR = 0L
OR = 1L
AND = 2L
NOT = 3L
CGADGETUP = 0L
CGADGETDOWN = 1L
CCHECKED = 2L
CDISABLED = 4L
CHIGHLIGHTED = 8L

# Constants (input events)

# Constants (input events)

E_IM_MASK = 0xE000FFFF
MSG_LEN = 320

# down, first repeat, invert
BUTTON_BASE = 0xE000 # Do not move
BUTTON1 = 0x10 + BUTTON_BASE
BUT
