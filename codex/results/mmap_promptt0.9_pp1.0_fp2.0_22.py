import mmap
# Test mmap.mmap return offset
# flush() writes every change and returns OS error code
# flush(len(data)) writes only part of data and returns OS error code

with open("p24_out.bin", "rb") as f6:
    byte_file = mmap.mmap(f6.fileno(), 0, access=mmap.ACCESS_WRITE)
    byte_file.seek(0)
    byte_file.write(enc_data[:int(len(enc_data)/2)])
    byte_file.flush(int(len(enc_data)/2))
    byte_file.write(enc_data[int(len(enc_data)/2):])
    byte_file.flush()
byte_file.close()
with open("p24_out.bin", "rb") as f7:
    print(f7.read())



# Challenge 25
# Use break_repeat_key_XOR() to decrypt
# Use a stream cipher to encrypt data
# Break it using break_ECB_mode as in challenge 12
# 1. Take a random key K, prepend
