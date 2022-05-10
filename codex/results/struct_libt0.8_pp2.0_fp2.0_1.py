import _struct
    #arg_list = list(msg_args)
    #arg_list[1] = True
    return _struct.pack(MSG_TYPE_2_STRUCT.get(msg_type, "H"), *msg_args[0:2]) + ''.join(msg_args[2:])

def get_msg_args(msg_type, msg_body):
    msg_struct_fmt = MSG_TYPE_2_STRUCT.get(msg_type, "H")
    args_len = struct.calcsize(msg_struct_fmt)
    return struct.unpack(msg_struct_fmt, msg_body[:args_len])

def get_msg_type(msg):
    return struct.unpack(">H", msg[:2])[0]

def get_msg_body(msg):
    return msg[2:]

def get_msg_length(msg):
    return struct.unpack(">H", msg[:2])[0]

def encode_msg(msg_type, msg_body):
    return struct.
