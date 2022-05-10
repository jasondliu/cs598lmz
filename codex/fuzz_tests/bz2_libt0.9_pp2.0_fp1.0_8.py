import bz2
bz2.decompress(compressed_data).decode("utf-8")

print("Compressed data size: ", len(compressed_data))


# Example 2: add compression to the shared memory using compression_type="zstd" (https://pypi.python.org/pypi/zstd).
datashm = numpy.random.randint(255, size=int(2e9))
manager = multiprocessing.Manager()
addr = manager.shm_addr_from_array(datashm, 'img', compression_type="zstd", level=1)
compressed_data = manager.shm_array_from_addr(addr, 'img', compression_type="zstd", level=1).copy().tostring()
zstd.decompress(compressed_data).decode("utf-8")
print("Compressed data size: ", len(compressed_data))


# Example 2: add a password to protect the shared memory and the contained data.
datashm = numpy.random.randint(255, size=int(2.5e9
