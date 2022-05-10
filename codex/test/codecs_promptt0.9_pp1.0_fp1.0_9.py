import codecs
# Test codecs.register_error()
CAN_REGISTER_ERRORS = True
try:
    codecs.register_error
except AttributeError:
    CAN_REGISTER_ERRORS = False
