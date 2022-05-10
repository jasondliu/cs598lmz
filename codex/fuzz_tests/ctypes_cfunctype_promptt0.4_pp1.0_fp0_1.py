import ctypes
# Test ctypes.CFUNCTYPE()
#
# This test is based on the following C code:
#
# #include <stdio.h>
# #include <stdlib.h>
#
# void print_int(int x) {
#     printf("%d\n", x);
# }
#
# void print_string(char *s) {
#     printf("%s\n", s);
# }
#
# void print_int_string(int x, char *s) {
#     printf("%d %s\n", x, s);
# }
#
# int main(void) {
#     void (*f1)(int);
#     void (*f2)(char *);
#     void (*f3)(int, char *);
#
#     f1 = print_int;
#     f2 = print_string;
#     f3 = print_int_string;
#
#     f1(42);
#     f2("hello");
#     f3(42, "hello");
#
#     return 0;
# }
#
# Comp
