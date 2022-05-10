import ctypes
# Test ctypes.CFUNCTYPE
func_ptr_type_t = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
def get_quotes_func_ptr(library_ptr):
    return library_ptr.get_quotes
get_quotes = func_ptr_type_t(get_quotes_func_ptr(library_ptr))
equities = ctypes.cast((ctypes.c_char_p * 4)("A", "B", "C", "D"), ctypes.POINTER(ctypes.c_char_p))
quotes_array_length = ctypes.c_int()
quotes_array = ctypes.cast(get_quotes(equities, 4, ctypes.byref(quotes_array_length)), ctypes.POINTER(ctypes.POINTER(QuoteStruct)))
quote_count = quotes_array_length.value
for i in xrange(quote_count):
    quote = quotes_array[i].contents
    print('%d:%d' % (quote.id, quote.price))
de
