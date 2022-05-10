import lzma
# Test LZMADecompressor.memory_size
#
# support.py: test-support@python.org
#
# Copyright (c) 2006 by the Python Software Foundation
# Copyright (c) 2007 by Georg Brandl
#
# Licensed under the Python License, version 2.0.
# See accompanying "NOTICE" file for more information.
#
# This is a copy of the test case for the Reference LZMA SDK
# http://www.7-zip.org/svn/trunk/CPP/7zip/Compress/LZMA_Alone/LZMABench.cpp@4762#L1680-L1681
#
# This file also is in the public domain.
import lzma
lzmabench={"data": "\x03\x00\x00\x00\x00\x00\x00\x00\xe0\xff\x41\x44\x44\x52\x01\x00\x42\x43\x56\x01\x00\x00\x00\x5d\x00\x00\x00\xb6\x
