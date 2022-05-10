import codecs
# Test codecs.register_error agains some codecs which support error handlers
# As of Unicode 3.2, some codecs don't yet work with the new error handling.
# See SF bug #947043.
import string

