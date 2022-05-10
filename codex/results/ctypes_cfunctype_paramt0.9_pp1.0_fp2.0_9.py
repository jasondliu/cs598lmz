import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t, ctypes.c_size_t)
lbn_block = libnacl.crypto_box_keypair # s: secret
lbn_seal = libnacl.crypto_seal # p: plaintext, p_len: plaintext length, b: block data key
lbn_unseal = libnacl.crypto_seal_open # b: seal, s: secret, p: plaintext, p_len: plaintext length
lbn_free = libnacl.crypto_free # b: seal, s: secret
lbn_blocked = FUNTYPE(libnacl.libnacl_num_blocked)
lbn_block_size = FUNTYPE(libnacl.libnacl_block_size)

def rabin_to_multi(fn_in, fn_out, block_size=None):
    blocks, bs = fm.block_file(fn_in, block_size)

    if not block_size
