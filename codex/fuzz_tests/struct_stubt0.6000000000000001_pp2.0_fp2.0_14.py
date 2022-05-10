from _struct import Struct
s = Struct.__new__(Struct)
s.__doc__ = '''
    This class is used to create byte format that is used to pack and unpack data.
    Following are the different format character that you can use in this class.

    Format Character  C Type          Python Type        Standard size
    ============      ========        ============       =============
    x                 pad byte        no value           1
    c                 char            bytes of length 1  1
    b                 signed char     integer            1
    B                 unsigned char   integer            1
    ?                 _Bool           bool               1
    h                 short           integer            2
    H                 unsigned short  integer            2
    i                 int             integer            4
    I                 unsigned int    integer            4
    l                 long            integer            4
    L                 unsigned long   integer            4
    q                 long long       integer            8
    Q                 unsigned long long integer         8
    f                 float           float              4
    d                 double          float              8
    s                 char[]          bytes              1
    p                 char[]          bytes              1
    P                 void *          integer            4
'''
