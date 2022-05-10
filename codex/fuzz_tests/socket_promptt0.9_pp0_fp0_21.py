import socket
# Test socket.if_indextoname()
#
(IF_NAMESIZE, IF_FLAGS) = (32, 64)
class ifreq(ctypes.Structure):
	_fields_ = [
		('ifr_ifrn', ctypes.c_char * IF_NAMESIZE),
		('ifr_name', ctypes.c_char * IF_NAMESIZE)]
class ifreq64(ctypes.Structure):
	_fields_ = [
		('ifr_ifrn', ctypes.c_char * IF_NAMESIZE),
		('ifr_name', ctypes.c_char * IF_NAMESIZE),
		('ifr_flags', ctypes.c_int32)]
class ifconf(ctypes.Structure):
	_fields_ = [
		('ifc_buf', ctypes.c_char_p),
		('ifc_len', ctypes.c_int32)]
def if_indextoname(ifindex):
	buf = ctypes.create_string_buffer(IF_NAMESIZE)
	s = socket
