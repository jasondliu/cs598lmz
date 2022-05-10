from _struct import Struct
s = Struct.__new__(Struct)

code_info = pydoc.resolve(code_info)
code_info.__doc__ += u'\n - :func:`code_info`'
s.__doc__ = code_info.__doc__
s.__code__ = code_info.__code__

#----------------------------------------------------------------------

def main():
	import sys, doctest
	if sys.flags.optimize:
		sys.stderr.write('This module cannot be run when optimized.\n')
		sys.exit(1)
	
	doctest.testmod()
	#doctest.testmod(sys.modules[__name__])

if __name__ == '__main__':
	main()
