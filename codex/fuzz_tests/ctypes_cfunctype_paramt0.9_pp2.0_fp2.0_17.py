import ctypes
FUNTYPE = ctypes.CFUNCTYPE(c_uint64)
get_time = FUNTYPE(("get_time", dll))

# bap/bap.h
c_bap_pid = c_uint32

#bap/disasm.h
bap_disasm_insn = c_void_p

#asmjit/asmjit.h
bap_asmjit_end = c_uint8

# bap/basic_types.h
bap_insn_kind = c_uint8

# bap/libbap.h
bap_image = c_void_p
bap_pid_t = c_uint32
bap_mem_segment = c_void_p
bap_pid_map = c_void_p
c_bap_mem = c_uint64

# ctypes_bap.h
c_bap_disasm_cnf = c_uint64

bap_disasm_init = CFUNCTYPE(c_int, c_char_p, c_bap_disasm_cnf, POINTER(c
