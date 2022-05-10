import ctypes
# Test ctypes.CField
#
# This test is here because it requires a class and a CField
# object, which are not available in the other test files.
#
# The testcase covers the following aspects of the CField
# implementation:
#
#   * Whether a simple field is accessible through
#     the CField object and the class
#
#   * Whether a simple field is readable and writable
#
#   * Whether a simple field is readable and writable
#     when the instance is a subtype
#
#   * Whether a simple field is readable and writable
#     when the instance is a subtype (2)
#
#   * Whether a simple field is readable and writable
#     when the instance is a supertype
#
#   * Whether a simple field is readable and writable
#     when the instance is a supertype (2)
#
#   * Whether a simple field is readable and writable
#     when the instance is a supertype (3)
#
#   * Whether a simple field is readable and writable
#     when the instance is a supertype (4)
#
#   *
