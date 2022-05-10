import codecs
# Test codecs.register_error
import locale
# Test locale.Error
import random
# Test random.Error
import re
# Test re.error and re.PatternError
import socket
# Test socket.error
import ssl
# Test ssl.SSLError
import struct
# Test struct.error
import zlib
# Test zlib.error
import _testcapi

# bpo-35777: This test should fail due to not enough arguments,
# however, -Werror=cpp turns it into a hard error
# _testcapi.test_include_error_msg

# bpo-35777: This test should fail due to not enough arguments,
# however, -Werror=cpp turns it into a hard error
# _testcapi.test_include_warn_msg

# bpo-35777: This test should fail due to not enough arguments,
# however, -Werror=cpp turns it into a hard error
# _testcapi.test_include_warn_msg_2

# bpo-35777: This test should fail due to not enough arguments,
# however, -Werror=cpp
