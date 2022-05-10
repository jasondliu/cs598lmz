import weakref
import ctypes
import ctypes.wintypes
import ctypes.util
import platform
import re
import socket

if platform.system() != "Windows":
	raise ImportError("This module only works on Windows.")

shell32 = ctypes.windll.shell32


def lookup_icon(icon_path, icon_index):
	'''Retrieves the handle to the specified icon resource.

	This function is equivalent to the SHORTPATH command,
	and uses SHGetFileInfoA to load icons.

	Arguments:
	`icon_path` - Path to the icon file.
	`icon_index` - Zero-based index of the group icon.
	'''

	return shell32.ExtractIconA(
		0, icon_path, icon_index
	)


