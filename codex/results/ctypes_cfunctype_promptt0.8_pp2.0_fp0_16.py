import ctypes
# Test ctypes.CFUNCTYPE
def set_proc_name(name):
	if not isinstance(name, bytes):
		raise TypeError
	libc = ctypes.CDLL("libc.so.6", use_errno=True)
	libc.prctl(15, name, 0, 0, 0)

@struct.struct()
class sock_filter(struct.structure):
	__byte_order__ = "big"
	__struct__ = """
		struct sock_filter { /* Filter block */
			__u16	code;   /* Actual filter code */
			__u8	jt;	/* Jump true */
			__u8	jf;	/* Jump false */
			__u32	k;      /* Generic multiuse field */
		};
	"""

@struct.struct()
class sock_fprog(struct.structure):
	__byte_order__ = "big"
	__struct__ = """
		struct sock_fprog {		/* Required for SO_ATTACH_FILTER. */
		
