import _struct
import sys
from Crypto.Cipher import AES
from Crypto import Random


def decrypt_file(key, filename):
    chunksize = 64 * 1024
    output_filename = filename[:-4]

    with open(filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(output_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)


decrypt_file('password', 'C://Users//Saju//Desktop//decryptor//test.bin')
