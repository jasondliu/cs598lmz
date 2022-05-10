import _struct

_BYTE_ORDER = 'big'
_HEADER_LEN = 8

_header_fmt = '>LL'
_header_struct = _struct.Struct(_header_fmt)

def pack_header(opcode, length):
    return _header_struct.pack(opcode, length)

def unpack_header(data):
    return _header_struct.unpack(data)

def pack_request(opcode, request_data):
    header = pack_header(opcode, len(request_data))
    return header + request_data

def unpack_request(data):
    opcode, length = unpack_header(data[:_HEADER_LEN])
    return opcode, data[_HEADER_LEN:_HEADER_LEN+length]

def pack_response(opcode, response_data):
    header = pack_header(opcode, len(response_data))
    return header + response_data

