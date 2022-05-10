import codecs
# Test codecs.register_error("test", codecs.ignore_errors)
#
# $ python python3.py
#
# Traceback (most recent call last):
#   File "python3.py", line 4, in <module>
#     codecs.register_error("test", codecs.ignore_errors)
# TypeError: 'module' object is not callable

import sys
# Test sys.stdin.buffer, sys.stdout.buffer, sys.stderr.buffer
#
# $ python python3.py
#
# Traceback (most recent call last):
#   File "python3.py", line 4, in <module>
#     with open(sys.stdin.buffer, "rb") as f:
# TypeError: expected str, bytes or os.PathLike object, not _io.BufferedReader

import dis
# Test dis.dis()
#
# $ python python3.py
#
# Traceback (most recent call last):
#   File "python3.py", line 4, in <module>
#     dis.dis(dis)
# TypeError: dis
