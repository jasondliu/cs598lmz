import codecs
# Test codecs.register_error
#
# This tests the basic functionality of codecs.register_error().
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTREPLACEMENT OR
# OTHER PRIOR WRITTEN CONSENT IS REQUIRED FOR ANY USE OF THIS
# SOFTWARE, INCLUDING commercial applications.
#
# $Id: test_register_error.py,v 1.2 2004/07/05 08:57:46 lemburg Exp $

import unittest
from test import test_support

# Codecs to be tested
import codecs

# Base class for the codec error handlers
class CodecError(Exception):
    pass

# Custom codec error handler
class MyCodecError(CodecError):
    pass

# Custom codec error handler
class MyOtherCodecError(CodecError):
    pass

# Custom codec error handler
class MyOtherOtherCodecError(CodecError):
    pass

# Custom codec error handler
class MyOtherOtherOtherCodecError(CodecError):
   
