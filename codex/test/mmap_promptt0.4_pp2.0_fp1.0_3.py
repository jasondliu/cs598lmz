import mmap
# Test mmap.mmap
#
# Test the mmap module's mmap objects.
#
# This test is a bit unusual in that it requires a file to be created
# before running.  The file should be approximately 8MB in size, and
# should be called "mmap_testfile".  On unix, "dd if=/dev/zero
# of=mmap_testfile bs=1024 count=8192" should create a suitable file.
#
# Note that this test is not exhaustive.  It only tests the methods
# that are actually used by the mmap module's own unit tests.
#
# XXXX To do:
#
# - Test move().
# - Test resizing (resize(), size(), etc.)
# - Test flush().
# - Test tagname() and tagid().
# - Test find().
# - Test rfind().
# - Test iterating over an mmap object.
# - Test getting slices, etc.
# - Test getting and setting single characters.
#
# Written by: Fred L. Drake, Jr. <fdrake@acm.org>
#
# $Id$

