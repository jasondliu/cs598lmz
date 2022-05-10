import _struct
# Test _struct.Struct_methods
import test.test_struct
test.test_struct.StructTest.test_Struct_methods.im_func(test.test_struct.StructTest)

import binascii
# Test binascii.b2a_uu
binascii.b2a_uu('')
binascii.b2a_uu('\x01')

import mmap
# Test mmap.mmap.close
import test.test_mmap
test.test_mmap.MmapTests.test_close.im_func(test.test_mmap.MmapTests)

import locale
# Test locale.format_string
import test.test_locale
test.test_locale.LocaleFormatTests.test_format_string.im_func(test.test_locale.LocaleFormatTests)

import _random
# Test _random.Random.seed
import test.test_random
test.test_random.RandomTest.test_seed.im_func(test.test_random.RandomTest)

import _cod
