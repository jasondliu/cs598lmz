import _struct

def p32(v):
    return _struct.pack('<I', v)

def u32(v):
    return _struct.unpack('<I', v)[0]

class ROP(object):
    def __init__(self, binary):
        self.r = process(binary)
        self.binary = binary

    def debug(self, breakpoints):
        text_base = self.binary.symbols['main']
        PIE = text_base
        script = 'pie base 0x{:x}\n'.format(PIE)
        for bp in breakpoints:
            script += 'b *0x{:x}\n'.format(PIE+bp)
        gdb.attach(self.r, gdbscript=script)

    def dump(self, addr, length=0x100):
        if length == 0:
            return ''
        with open('/proc/{}/mem'.format(self.r.pid), 'rb') as mem:
            mem.seek(addr)
            return mem.read(length)

   
