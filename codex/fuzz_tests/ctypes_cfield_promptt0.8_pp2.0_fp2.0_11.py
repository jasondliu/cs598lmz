import ctypes
# Test ctypes.CField flag with structure members
#
# RUN: python %s | llc -mtriple=x86_64-apple-darwin | FileCheck %s

for test in [ ('char', 'C'), ('unsigned char', 'B'), ('short', 'h'),
              ('unsigned short', 'H'), ('int', 'i'), ('unsigned int', 'I'),
              ('long', 'l'), ('unsigned long', 'L'), ('long long', 'q'),
              ('unsigned long long', 'Q'), ('float', 'f'), ('double', 'd') ]:
   print("""
%s
typedef struct {
    char x;
    %s y;
} A;
""" % (test[1], test[0]))
   class A(ctypes.Structure):
       _fields_ = [("x", ctypes.c_char), ("y", ctypes.CField(test[1]))]
   a = A()
   a.x = 'M'
   a.y = 10
   print "@a = global %struct.A %a"
   print "define void @
