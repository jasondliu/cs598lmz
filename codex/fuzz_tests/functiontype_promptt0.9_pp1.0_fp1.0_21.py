import types
# Test types.FunctionType assumption
assert issubclass(types.FunctionType, types.CodeType)
def _print_exception(message):
	print('*** ERROR: %s' % message)

def _print_exception_error(message):
	print('*** ERROR: %s' % message)

def _print_exception_raise(message):
	raise Exception(message)

_print_exception = _print_exception_raise

_DecodedLine = namedtuple('_DecodedLine', 'in_function pc_offset ext_offset self_offset ext_is_constant self_is_constant')
def _decode_addr(ext_addr, const_addr, self_addr, pc_offset = 0,
				in_function = False):
	return _DecodedLine(in_function, pc_offset, ext_addr,
					self_addr, ext_addr >= 0, self_addr >= 0)

# These are completely arbitrary constants.
# 0x.../0x...
CONST_ADDR_OFFSET = 0x800000

