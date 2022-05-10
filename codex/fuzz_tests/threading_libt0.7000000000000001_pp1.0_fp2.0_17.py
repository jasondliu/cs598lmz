import threading
threading.stack_size(67108864)

sys.path.insert(0, './lib')

from my_crypto_lib import *

mode = AES.MODE_CBC

def decrypt(ciphertext, key, iv=None):
    aes = AES.new(key, mode, iv)
    plaintext = aes.decrypt(ciphertext)
    return plaintext

def encrypt(plaintext, key, iv=None):
    aes = AES.new(key, mode, iv)
    ciphertext = aes.encrypt(plaintext)
    return ciphertext

def cbc_mac(ciphertext, key, iv=None):
    aes = AES.new(key, mode, iv)
    cbc_mac = aes.encrypt(ciphertext)[-16:]

    return cbc_mac

def wy_cbc_mac(ciphertext, key, iv=None):
    aes = AES.new(key, mode, iv)
    cbc_mac = aes.encrypt(ciphertext)[
