import mmap
import cv2
import os
import ctypes
import sys

debug = False

RESX = 16384
RESY = 16384

centerX = RESX/2
centerY = RESY/2

def get16BitValue(bytes, a=False):
	if a:
		n = ord(bytes[0]) << 8 | ord(bytes[1])
		if n >= 2**15:
			n -= 2**16
		return n
	else:
		return ord(bytes[0]) << 8 | ord(bytes[1])

def get32BitValue(bytes, a=False):
	if a:
		n = ord(bytes[0]) << 24 | ord(bytes[1]) << 16  | ord(bytes[2] << 8) | ord(bytes[3])
		if n >= 2**31:
			n -= 2**32
		return n
	else:
		return ord(bytes[0]) << 24 | ord(bytes[1]) << 16  | ord(bytes[2] << 8)
