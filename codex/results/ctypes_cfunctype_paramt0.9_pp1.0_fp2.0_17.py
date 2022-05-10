import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, POINTER(DispatchMgr))

#CMPXCHG
LOADPTR	= 1
CMPPTR	= 2
STOREPTR= 3
LOAD32	= 4
CMP32	= 5
STORE32	= 6

#Freeze commands
MD_FREEZE_LOAD_CMD	= 1
MD_FREEZE_ISA_CMD	= 2
MD_FREEZE_CMD_DONE	= 3
MD_FREEZE_CMD_ERROR	= 4

class DispatchMgr(ctypes.Structure):
	_fields_	= []

class CpuState(ctypes.Structure):
	_fields_	= [('eax', ctypes.c_uint), ('ecx', ctypes.c_uint), ('edx', ctypes.c_uint), ('ebx', ctypes.c_uint), ('esp', ctypes.c_uint), ('ebp', ctypes.c_uint), ('esi', ctypes.c_uint), ('edi', ctypes.c_uint)]

class DataTarg(ctypes.
