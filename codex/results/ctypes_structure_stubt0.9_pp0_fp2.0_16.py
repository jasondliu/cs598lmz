import ctypes

class S(ctypes.Structure):
    x = ctypes.c_longlong
    y = ctypes.c_longlong

rt = ctypes.CDLL('librtl.so')
code = b'\x48\x83\x4f\x09\x05'
rt.rt_exec_code(code, ctypes.sizeof(code), ctypes.pointer(S()), ctypes.sizeof(S()))
</code>
The C code could be
<code>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

void rt_exec_code(unsigned char* code,
                  size_t codelen,
                  void* insn_mem,
                  size_t insn_mem_size) {
    fprintf(stderr,"%p &lt; %p", code, code+codelen);
    fprintf(stderr,"%p &lt; %p", insn_mem, insn_mem+insn_mem_size);
    memcpy(insn_mem, code, codelen);
   
