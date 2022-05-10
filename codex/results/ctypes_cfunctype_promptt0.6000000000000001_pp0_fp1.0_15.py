import ctypes
# Test ctypes.CFUNCTYPE()'s
#  - struct-returning functions
#  - struct-returning functions returning pointers
#  - struct-returning functions returning unions
#
# See also:
#  http://www.codesourcery.com/public/cxx-abi/abiflags.html
#  http://www.codesourcery.com/public/cxx-abi/abi.html#mangling
#
# The C++ ABI defines the mangled names of functions returning structs as:
#
#   <return-type> <function-name> (<parameter-types>)
#
# For example:
#
#   struct S {
#     int a;
#     int b;
#   };
#
#   struct S f(int x) {
#     struct S s;
#     s.a = x;
#     s.b = x+1;
#     return s;
#   }
#
#   struct S g(int x) {
#     return (struct S) { x, x+1 };
#   }
#
# The mangled
