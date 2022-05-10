import weakref
# Test weakref.ref function
# import test.test_weakref
# if you see "test_weakref passed all tests" at the end, you know that
# weakref.ref() is available.
#
# Beware, this module depends on a patched version of
# Zope's ZPublisher and ZPublisher.HTTPResponse.
#
# This version has a small bugfix in ZPublisher.HTTPResponse:
# in _unauthorized() it does not set WWW-Authenticate header.
#
# Also in ZPublisher.HTTPResponse, a new function
# _unauthorized_token() was implemented.
#
# All changes marked with 'XXX: UNIT TESTS:'.
#
# The test folder contains a diff of the changes.
#
# Steps to apply these changes:
#
# 1. Unpack Zope sources in your Zope 3.0.0 installation.
#
#    Note: the changes I made were tested in Zope
#          CVS of 2004-05-20, not in the latest snapshot.
#          There's a chance that the changes are already
#         
