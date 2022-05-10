import socket
socket.if_indextoname('2')

from ctypes import *
import win32netcon
import socket
Advapi32 = windll.advapi32

class DNS_RPC_RECORD(Structure):
_fields_ = [
	('wType', c_ushort),
	('wDataLength', c_ushort),
	('flags', c_ulong),
	('dwTtl', c_ulong),
	('dwReserved', c_ulong),
	('Data', c_ubyte * 1)
	]

class DNS_RPC_HEADER(Structure):
_fields_ = [
	('xid', c_ulong),
	('flags', c_ushort),
	('qCount', c_ushort),
	('aCount', c_ushort),
	('nsCount', c_ushort),
	('arCount', c_ushort)
	]

class DNS_RPC_QUESTION(Structure):
_fields_ = [
	('QuestionName', c_wchar * 256),
	('QuestionType', c_ushort
