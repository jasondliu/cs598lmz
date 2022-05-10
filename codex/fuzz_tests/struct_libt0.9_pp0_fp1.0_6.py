import _struct

def _udecode(istream, frame):
	# U: unsigned format of i, see below
	# u: Py_UNICODE low-level storage, either UCS-1 or UCS-4, subject
	#    to the setting of sys.maxunicode
	# d: Decoded Python Unicode, using \uXXXX escapes or \UXXXXXXXX escapes
	#    if it requires non-BMP characters
	# p: Printable ASCII string ending with ASCII NUL byte
	#   (but only if the Unicode is entirely ASCII)
	# s: UTF-8-encoded Unicode string, including the NUL byte if it's a
	#    printable ASCII string
	# h: Hexadecimal representation of the Unicode as 8-bit bytes, in
	#    '0123456789abcdef'
	#    (if not a printable ASCII string)
	# g: Unicode character name, according to the Unicode database
	# c: one-character Unicode string

	try:
		return _long(istream.read(4))
	except:
		frame.pop(
