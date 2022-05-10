import mmap
import struct
import sys
import time

# Definitions

# I/O access
IODIRA = 0x00  # IO direction A - 1= input 0 = output
IODIRB = 0x01  # IO direction B - 1= input 0 = output

# Input polarity A - If a bit is set, the corresponding GPIO register bit
# will reflect the inverted value on the pin.
IPOLA = 0x02

# Input polarity B - If a bit is set, the corresponding GPIO register bit
# will reflect the inverted value on the pin.
IPOLB = 0x03

# The GPINTEN register controls the interrupt-onchange feature for each
# pin.
GPINTENA = 0x04  # Interrupt enable A
GPINTENB = 0x05  # Interrupt enable B

# Default value for port A - These bits set the compare value for pins
# configured for interrupt-on-change. If the associated pin level is the
# opposite from the register bit, an interrupt occurs.
DEFVALA = 0x06

# Default value for port B - These bits set the
