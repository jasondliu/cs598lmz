import _struct
from config import settings
from structs import structs
from structs.structs import *
from utils.converters import *
from utils.enums import *
from utils.utils import *

# Unpack function
def unpack(data):
    buffer = {}
    buffer['version'] = data[0]
    buffer['msgType'] = data[1]
    unpack_buffer = data[2:]

    # Check version
    if buffer['version'] != settings.VERSION:
        raise ValueError('Wrong protocol version (%s) in request' % buffer['version'])

    # Check message type
    if buffer['msgType'] != settings.MSG_TYPE:
        raise ValueError('Wrong message type (%s) in request' % buffer['msgType'])

    # Unpack the message type and the request type
    msgType, requestType = unpack_buffer[:2]
    buffer['msgType'] = msgType
    buffer['requestType'] = requestType
    unpack_buffer = unpack_buffer[2:]

    # Call the associated function
   
