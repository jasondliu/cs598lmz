import ctypes
# Test ctypes.CFUNCTYPE

# This is a test of ctypes.CFUNCTYPE.
#
# The test is based on the following C code:
#
#   #include <stdio.h>
#
#   typedef void (*f_t)(int);
#
#   void f(int i) {
#       printf("f(%d)\n", i);
#   }
#
#   void g(f_t f) {
#       f(1);
#   }
#
#   void h(f_t f) {
#       f(2);
#   }
#
#   int main(void) {
#       g(f);
#       h(f);
#       return 0;
#   }
#
# The test is run by compiling the above C code and running it.
# The output should be:
#
#   f(1)
#   f(2)
#
# The test is run by compiling the above C code and running it.
# The output should be:
#
#   f(1)
#   f(2
