import ctypes
# Test ctypes.CField structure
#
#     typedef struct _fieldobject {
#         PyObject_HEAD
#         PyTypeObject *f_type; /* Declared type */
#         union {
#             int *i;
#             long *l;
#             float *f;
#             double *d;
#             signed char *b;
#             unsigned char *B;
#             short *h;
#             unsigned short *H;
#             long long *q;
#             unsigned long long *Q;
#             char *s;
#             void *p;
#         } f_loc;
#         char *f_name;
#         int f_offset;
#         int f_size;
#         int f_pack;
#     } PyCFieldObject;
#
# f_loc.s is the first field we can use

# This is what ctypes.cfield raises, it doesn't support all types
# TypeError: expected c_char_p_p, got c_char_p
#
# The following also doesn't work
# class POINT(ctypes.St
