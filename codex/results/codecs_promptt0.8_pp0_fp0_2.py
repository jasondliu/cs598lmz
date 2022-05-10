import codecs
# Test codecs.register_error()
def add(t,f):
	def g(c):
		e=t(c)
		if e==UnicodeEncodeError:
			return f(c)
		return e
	return g
codecs.register_error(add(codecs.lookup_error('strict'),lambda c:('?',None)))
codecs.lookup_error('strict')
#Test lookup_error()
for i in ['strict','replace','ignore','xmlcharrefreplace','backslashreplace']:
	codecs.lookup_error(i)
# Test BOM_UTF8
BOM_UTF8=codecs.BOM_UTF8
BOM_BE=codecs.BOM_BE
BOM_LE=codecs.BOM_LE
codecs.BOM_UTF16
codecs.BOM_UTF16_BE
codecs.BOM_UTF16_LE
codecs.BOM_UTF32
codecs.BOM_UTF32_BE
codecs
