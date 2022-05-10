import codecs
# Test codecs.register_error()
def add(t,f):
	def g(c):
		e=t(c)
		if e==UnicodeEncodeError:
			return f(c)
		return e
	return g
