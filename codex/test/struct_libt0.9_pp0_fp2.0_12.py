import _struct
from array import array

http_1_1_parser_module = C.CDLL(find_library('http_1_1_parser'))
http_1_1_parser_module.HTTP_REQUEST_PARSER_init.argtypes = [C.POINTER(C.c_int), C.POINTER(C.c_void_p)]
http_request_parser_init = http_1_1_parser_module.HTTP_REQUEST_PARSER_init
http_request_parser_init.restype = C.c_int

http_1_1_parser_module.HTTP_REQUEST_PARSER_feed.argtypes = [C.c_void_p, C.POINTER(C.c_char), C.POINTER(C.c_int), C.POINTER(C.c_int)]
http_request_parser_feed = http_1_1_parser_module.HTTP_REQUEST_PARSER_feed
http_request_parser_feed.restype = C.c_int

http_1_1_parser_module.HTTP_
