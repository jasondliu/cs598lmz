import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is a bit more involved than the others, because there are
# so many things that can go wrong.  We want to test the following
# things:
#
# 1) That the function is called.
# 2) That the function is called with the right arguments.
# 3) That the function is called with the right argument types.
# 4) That the function is called with the right return type.
# 5) That the function is called with the right calling convention.
# 6) That the function is called with the right calling convention
#    when the function is a member of a class.
#
# To test all of these, we create a function in C that does the
# following:
#
# 1) Takes a set of arguments, and compares them to a set of
#    expected arguments.  If they match, it returns 1.  Otherwise,
#    it returns 0.
# 2) Takes a set of arguments, and compares them to a set of
#    expected arguments.  If they match, it returns a pointer to a
#    string.  Otherwise, it returns NULL.
# 3) Takes
