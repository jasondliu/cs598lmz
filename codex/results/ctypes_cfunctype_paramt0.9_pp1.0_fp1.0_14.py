import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def build_find_last_byte(find_last_byte_code, byte):
    new_find_last_byte_code = asm(
    '''
    mov r11, rdi
    xor rdi, rdi
    mov dil, {byte}
    call {find_last_byte}
    ret
    '''.format(byte=byte, find_last_byte=hex(find_last_byte_code)),
    vma=find_last_byte_code)
    find_last_byte_ctype = FUNTYPE(int)
    return new_find_last_byte_code, find_last_byte_ctype

def build_set_bit(set_bit_code):
    new_set_bit_code = asm(
    '''
    mov al, {offset}
    shl al, cl
    or [rdi], al
    ret
    '''.format(set_bit=hex(set_bit_code), offset=1),
    vma=set_bit_code
    )
    set_bit_ct
