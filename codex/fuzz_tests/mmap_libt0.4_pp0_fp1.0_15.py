import mmap
import struct
import sys
import time

# I/O access
IODIRA = 0x00 # Pin direction register
IODIRB = 0x01
IOCON = 0x0A # Pin configuration register
GPPUA = 0x0C # Pull-up resistor configuration register
GPPUB = 0x0D
GPIOA = 0x12 # Port register
GPIOB = 0x13

# Define GPIO pins
GPIO_A0 = 0x01
GPIO_A1 = 0x02
GPIO_A2 = 0x04
GPIO_A3 = 0x08
GPIO_A4 = 0x10
GPIO_A5 = 0x20
GPIO_A6 = 0x40
GPIO_A7 = 0x80

GPIO_B0 = 0x01
GPIO_B1 = 0x02
GPIO_B2 = 0x04
GPIO_B3 = 0x08
GPIO_B4 = 0x10
GPIO_B5 = 0x20
GPIO_B6 = 0x40
GP
