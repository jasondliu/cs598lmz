import _struct

def p32(v):
    return struct.pack('<I', v)

def u32(v):
    return struct.unpack('<I', v)[0]

def p64(v):
    return struct.pack('<Q', v)

def u64(v):
    return struct.unpack('<Q', v)[0]

def alloc(size):
    r.sendlineafter('choice: ', '1')
    r.sendlineafter('size: ', str(size))

def fill(idx, size, content):
    r.sendlineafter('choice: ', '2')
    r.sendlineafter('idx: ', str(idx))
    r.sendlineafter('size: ', str(size))
    r.sendafter('content: ', content)

def free(idx):
    r.sendlineafter('choice: ', '3')
    r.sendlineafter('idx: ', str(idx))

def dump(idx):
    r.sendlineafter('choice: ', '4')

