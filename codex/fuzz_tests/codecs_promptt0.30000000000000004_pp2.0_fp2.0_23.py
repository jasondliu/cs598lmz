import codecs
# Test codecs.register_error
#
# This test is intended to test the codecs.register_error function.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTREPLACE_ME WARRANTY.
#
# *** NOTE *** : the codecs module uses a rather complex error
# handling strategy. To test the error handler, we first need to
# understand this strategy.
#
# The codecs module defines the following exception classes:
#
# 1. LookupError
#    This exception is raised when a codec lookup fails; it is a
#    subclass of IndexError.
#
# 2. CodecError
#    This exception is raised when a codec encoding or decoding
#    fails. It is a subclass of UnicodeError.
#
# 3. UnicodeError
#    This exception is raised when a Unicode related encoding or
#    decoding error occurs. It is the base class for all Unicode
#    related error exceptions.
#
# 4. UnicodeEncodeError
#    This exception is raised when a Unicode related encoding
#    error occurs. It
