import bz2
# Test BZ2Decompressor for a valid file,
# and test the remaining part is empty after decompressing
bzf = bz2.BZ2File(ENVIRONMENT_CONFIG_NAME)
decompressor = bz2.BZ2Decompressor()
# (decompress all)
bzf.read()
result = decompressor.decompress()
decompressor.flush()
bzf.close()
print('env_config decompressed len:', len(result))
# assert len(result) > 0


from playsound import playsound

# playsound('keepsilence.mp3')
playsound('dingdingdingdingdingdingdingdingdingdingdingns.mp3')
