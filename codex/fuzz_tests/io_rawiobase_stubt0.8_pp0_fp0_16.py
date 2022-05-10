import io
class File(io.RawIOBase):
	"""File(filename, mode='r', buffering=-1)

	Open a file.  The mode can be 'r', 'w', 'x', 'a' or 'b'.  The default
	is to open files in text (translated) mode.  In this mode, if encoding
	is not specified the encoding used is platform dependent.  (For reading
	and writing raw bytes use binary mode and leave encoding unspecified.)
	The available modes are:

	========= ===============================================================
	Character Meaning
	--------- ---------------------------------------------------------------
	'r'       open for reading (default)
	'w'       open for writing, truncating the file first
	'x'       create a new file and open it for writing
	'a'       open for writing, appending to the end of the file if it exists
	'b'       binary mode
	't'       text mode (default)
	========= ===============================================================

	The default mode is 'rt' (open for reading text). For binary random
	access, the mode 'w+b' opens and truncates the file to 0 bytes, while
	'r+
