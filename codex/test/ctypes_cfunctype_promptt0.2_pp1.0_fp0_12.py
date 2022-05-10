import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test_ctypes.py test_cfunctype test.
#
# The test_cfunctype test is based on the following C code:
#
#   typedef int (*FUNC)(int, int);
#
#   int add(int a, int b) {
#       return a + b;
#   }
#
#   int sub(int a, int b) {
#       return a - b;
#   }
#
#   int mul(int a, int b) {
#       return a * b;
#   }
#
#   int div(int a, int b) {
#       return a / b;
#   }
#
#   int mod(int a, int b) {
#       return a % b;
#   }
#
#   int neg(int a) {
#       return -a;
#   }
#
#   int main(void) {
#       FUNC funcs[] = {add, sub, mul, div, mod, neg};
#       int
