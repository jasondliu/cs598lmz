import _struct
import _util
import _xor

__all__ = ['AES', '_AES', 'CCM', 'CMAC', 'CCMP', 'TKIP', 'GCM']

class AES(object):

    block_size = 16

    @classmethod
    def new(cls, key, mode):
        """Create a new AES object that can encrypt or decrypt str objects.

        key = raw string containing the key
        mode = AES mode string

        """
        aes = _AES()
        aes.setkey_encrypt(key)
        return AESModeOfOperation(aes, mode)

    @classmethod
    def new_cbc_encrypt(cls, key, iv):
        """Create a new AES object that can encrypt str objects.

        key = raw string containing the encryption key
        iv = raw string containing the initialization vector

        """
        aes = _AES()
        aes.setkey_encrypt(key)
        return AESModeOfOperationCBCEncrypt(aes, iv)

    @classmethod
    def new_c
