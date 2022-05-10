import io
# Test io.RawIOBase
import codecs
# Test codecs.IncrementalEncoder

try:
    import _testbuffer
except ImportError:
    pass
else:
    # Test _testbuffer.c_write_buffer
    pass
# Test bytearray
# Test memoryview
# Test bytes

# Test promise
# Test "0x0"

# Test odict
import collections
# Test collections.OrderedDict
import argparse
# Test argparse.Namespace
# Test argparse.ArgumentParser
import types
# Test types.MemberDescriptorType
# Test types.GetSetDescriptorType
# Test types.MethodDescriptorType
# Test types.MethodWrapperType
# Test types.WrapperDescriptorType

import os
# Test os.DirEntry

# Test classobj
# Test 'class'

# Test "PyObject_Print"

# Test cStringIO
import io
# Test io.BytesIO
import gzip
# Test gzip.GzipFile

# Test range

# Test reference
import weakref
# Test weakref
