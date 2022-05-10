import lzma
lzma.decompress(data)

# AES
# AES uses a symmetric key, meaning the same key is used to encrypt and decrypt the data.
# AES uses a key schedule to expand a short key into a number of separate round keys.
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

password = b'This is the password'
salt = b'This is the salt'

key = PBKDF2(password, salt)
print('KEY:', key)

iv = b'This is the IV456'

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = b'This is the message to be encrypted'
print('PLAINTEXT:', plaintext)

msg = iv + cipher.encrypt(plaintext)
print('ENCRYPTED:', msg)

cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(msg)[len(iv):]
print('DECRYPTED:', plaintext)

# RSA
# RSA
