import _struct
from ctypes import *


# from ctypes import *
#
#
# #
# # C++ ctypes
# #
# # typedef int8_t          INT8;
# # typedef int16_t         INT16;
# # typedef int32_t         INT32;
# # typedef int64_t         INT64;
# # typedef uint8_t         UINT8;
# # typedef uint16_t        UINT16;
# # typedef uint32_t        UINT32;
# # typedef uint64_t        UINT64;
#
# lib = cdll.LoadLibrary('./lib/lib_cc.so')
#
#
# def get_func(name, arg_types, res_types):
#     c_arg_types = [c_int]
#     for arg_type in arg_types:
#         if arg_type in ['int', 'int8', 'int16', 'int32', 'int64', 'uint8', 'uint16', 'uint32', 'uint64']:
#            
