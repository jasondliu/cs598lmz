import mmap
import sys

# Message type
MSG_TYPE_COMMAND  = 0x00
MSG_TYPE_EVENT    = 0x01
MSG_TYPE_RESPONSE = 0x02

# Command ID
CMD_ID_GET_BOARD_NAME = 0xA0

# Event ID
EVT_ID_BOARD_NAME = 0xA0

# Response ID
RESP_ID_BOARD_NAME = 0xA0

def read_message(fd):
    msg_type = ord(fd.read(1))
    msg_len  = ord(fd.read(1))
    msg_data = fd.read(msg_len)

    return msg_type, msg_len, msg_data

def read_string(data):
    n = ord(data[0])
    return data[1:n+1]

def write_message(fd, msg_type, msg_id, msg_data):
    msg_len  = len(msg_data)
    msg_type = chr(msg_type)
