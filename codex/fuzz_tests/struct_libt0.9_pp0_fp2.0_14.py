import _struct

# VGA constants
(VGA_CLOCK, VGA_COLORS) = (14318181, 0x100)

# Video mode constants
(VID_HWCURSOR, VID_CP437) = (0x1, 0x2)

# Console cursor state
class Cursor(Structure):
  _fields_ = [("col", c_short), ("row", c_short), ("shape", c_char)]

# Console constants
(CON_COLS, CON_ROWS) = (80, 25)
(CON_ECHO, CON_BUF, CON_HWCURSOR) = (0x1, 0x2, 0x4)

(CON_NORM, CON_RESET) = (0, 0)
(CON_RAW, CON_RAW1) = (1, 2)

# Console cursor state
(CON_HIDE, CON_MOVE, CON_SHOW) = (0, 1, 2)

# Framebuffer constants
FB_ADDR = 0x000a0000

# PC speaker constants
SPK_SET
