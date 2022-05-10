import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_char_p, ctypes.c_size_t)

def aes_crypt(data, key, iv, decrypt, padding):
    enc = 1
    if decrypt:
        enc = 0

    keylen = len(key)
    if keylen == 16 :
        keylen = 128
    elif keylen == 24 :
        keylen = 192
    elif keylen == 32 :
        keylen = 256
    else :
        raise ValueError("key must be 16, 24 or 32 bytes long")

    buf = ctypes.create_string_buffer(data)
    out = ctypes.create_string_buffer(len(data))
    ctx = ctypes.c_void_p(0)
    ctx = aes_init(key, keylen)
    if iv:
        aes_cbc_encrypt(ctx, buf, out, len(data), iv, enc)
    else :
        aes_ctr_encrypt(ctx, buf, out, len(data), iv)
    aes
