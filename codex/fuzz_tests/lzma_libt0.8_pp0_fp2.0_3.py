import lzma
lzma.LZMADecompressor().decompress(c)

# The first bit of the compressed is '\x5d'
# So it starts with ']', which is the output of magic_start
# After decompressing, the it ends with '}', which is the output from magic_end
# If the valid flag is appended to the end, it will output
# '}', 'congratz'
# But it will throw EOFError if and only if the valid flag is appended
# So we can assume that the flag is not appended
# And we are supposed to append the valid flag
# The valid flag is "flag{"
# So the flag shoule be
# flag{qwertyuioasdfghjkzxcvbnm_\x1bkK1\x04\x00\xf9\x00\x00\x00\x00\x1b\\[\x00\x00\x00\x00\xa0\x90"

print(c,c[0],c[-1],c[-2],c[-3])
