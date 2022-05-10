import _struct
import _sys

def _decode_pointer(instructions, pointer):
    offset = 0
    for i in instructions:
        if i[0] == 'ptr':
            pointer += i[2] * i[1]
        elif i[0] == 'lit':
            pointer += 1
        else:
            offset += struct.calcsize(i[0])
        if pointer < offset: return -1
    return pointer-offset

def _encode_insn(insn, val):
    v = val
    if insn[0] == 'ptr':
        while v > 0xffffffff:
            yield ('ptr', 4, 1)
            v -= 0x100000000
        yield ('ptr', 4, v)
    else:
        while v > 0xff:
            yield ('char', 'B', 1)
            v -= 0x100
        yield ('char', 'B', v)

def _i386_cs(**state):
    if state.get('arch') != 'i386': return []
    if state.get('bits') !=
