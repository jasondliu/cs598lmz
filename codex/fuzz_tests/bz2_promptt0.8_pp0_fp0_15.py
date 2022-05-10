import bz2
# Test BZ2Decompressor objects
#
# The test files used by this test were compressed using
# bzip2 --test and unbzip2 --test, with the --ignore-trailing-garbage option.
# This was to allow us to write to the end of the file without having the
# decompressor complain about the extra trailing garbage.
#
# The files used by this test are compressed versions of the following
# strings of data:
#
# 'BZh9\x00\x00' (12 bytes)
# 'BZh91AY&SY\x94\x0e\x00\x00\x01\x05\x00\x00\x004\x00' (32 bytes)
# 'BZh91AY&SY\xd2P\x00\x00\x0f\xfe\x00\x00\x0f\xaa' (32 bytes)
# 'BZh91AY&SY\x80\x00\x00\x00\x00\xff\xff\xff\xff' (32 bytes)
#
TEST_STRING1 = 'BZh9
