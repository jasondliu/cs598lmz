import codecs
# Test codecs.register_error('test', codecs.replace_errors)
# with codecs.open('/etc/resolv.conf', 'r', encoding='ascii', errors='test') as f:
#     print(f.read())

# class Codec:
#     def encode(self, input, errors='strict'):
#         return codecs.charmap_encode(input, errors, encoding_map)
#
#     def decode(self, input, errors='strict'):
#         return codecs.charmap_decode(input, errors, decoding_map)
#
# codecs.register(Codec().encode)
# codecs.register(Codec().decode)

# from ctypes import *
# libc = CDLL('libc.so.6')
# message_string = 'Hello World!'
# libc.printf('Testing: %s\n', message_string)

# from ctypes import *
# libc = CDLL('libc.so.6')
# class POINT(Structure):
#     _fields_ = [
