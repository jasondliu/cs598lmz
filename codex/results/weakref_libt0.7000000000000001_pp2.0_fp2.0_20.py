import weakref
import array
import ctypes

# The size of the pixel array.
PIXEL_COUNT = 32
# The number of pixels in each row.
PIXEL_ROW_COUNT = 4
# The number of rows in the display.
PIXEL_COL_COUNT = 8

# The number of bytes in the pixel array.
PIXEL_BUFFER_SIZE = PIXEL_COUNT * 3
# The number of bytes in each row.
ROW_SIZE = PIXEL_ROW_COUNT * 3
# The number of bytes in each column.
COL_SIZE = PIXEL_COL_COUNT * ROW_SIZE

# The I2C address of the display.
I2C_ADDRESS = 0x60

# The I2C commands for the display.
CMD_AUTOPLAY1 = 0xA1
CMD_AUTOPLAY2 = 0x9F
CMD_BLINK0 = 0x81
CMD_BLINK1 = 0x83
CMD_BRIGHTNESS = 0xE0
CMD
