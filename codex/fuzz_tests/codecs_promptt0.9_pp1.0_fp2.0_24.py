import codecs
# Test codecs.register_error('ignore', codecs.lookup_error("surrogateescape"))?
# It's mentioned in http://bugs.python.org/review/1029/
encoding = "utf-8"

def isIncomplete(s):
	return s.endswith("\uFFFD")

def stripIncomplete(s):
	return s.rstrip("\uFFFD")

def decode(s, encoding=encoding, errors='surrogateescape'):
	return s.decode(encoding, errors)

def encode(u, encoding=encoding, errors='surrogateescape'):
	return u.encode(encoding, errors)
