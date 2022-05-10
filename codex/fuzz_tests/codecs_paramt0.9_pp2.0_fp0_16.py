import codecs
codecs.register_error('cutf8',errors='ignore')

class UnicodeReader(object):
	'''
	A CSV reader which will iterate over lines in the CSV file "f",
	which is encoded in the given encoding.
	'''

	def __init__(self, f, dialect=csv.excel, encoding="utf8", **kwds):
		f = UTF8Recoder(f, encoding)
		self.reader = csv.reader(f, dialect=dialect, **kwds)

	def next(self):
		row = self.reader.next()
		return [unicode(s, "utf-8").encode("utf-8").strip() for s in row]

	def __iter__(self):
		return self

class UnicodeWriter:
	'''
	A CSV writer which will write rows to CSV file "f",
	which is encoded in the given encoding.
	'''

	def __init__(self, f, dialect=csv.excel, encoding="utf8", **kwds):
		# Redirect output to a queue
	
