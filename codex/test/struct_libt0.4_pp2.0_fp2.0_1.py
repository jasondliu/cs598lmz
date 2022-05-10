import _struct

from . import _compat


class _OpenSSL_Cipher_Ctx(object):
    def __init__(self, cipher, key, iv, op):
        self._cipher = cipher
        self._ctx = _ffi.new("EVP_CIPHER_CTX *")
        _lib.EVP_CIPHER_CTX_init(self._ctx)
        self._key_as_bytes = _ffi.new("unsigned char[]", key)
        self._iv_as_bytes = _ffi.new("unsigned char[]", iv)
        self._op = op
        self._update_outlen = 0
        self._final_outlen = 0
        self._finalized = False
        self._block_size = cipher.block_size
        self._key_size = cipher.key_size
        self._iv_size = cipher.iv_size

    def __del__(self):
        _lib.EVP_CIPHER_CTX_cleanup(self._ctx)

