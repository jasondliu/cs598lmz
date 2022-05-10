import codecs
codecs.register_error("strict", codecs.ignore_errors)


# JSON-RPC message types.
MESSAGE_REQUEST = 0
MESSAGE_RESPONSE = 1
MESSAGE_NOTIFICATION = 2

# JSON-RPC error codes.
ERROR_PARSE_ERROR = -32700
ERROR_INVALID_REQUEST = -32600
ERROR_METHOD_NOT_FOUND = -32601
ERROR_INVALID_PARAMS = -32602
ERROR_INTERNAL_ERROR = -32603
ERROR_SERVER_ERROR = -32000

# Characters used for generating random IDs.
ID_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# The maximum number of elements that can be held in each message.
MAX_ELEMENTS = 1000

# A UTF-8 encoder.
ENCODER = codecs.getencoder("utf-8")


class JSONRPCProtocolError(ProtocolError):
    """
