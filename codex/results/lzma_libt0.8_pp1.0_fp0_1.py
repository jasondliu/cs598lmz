import lzma
lzma.LZMA_FILTER_LZMA2

filename = sys.argv[1]
algorithm = int(sys.argv[2])
num_filters = int(sys.argv[3])

def compress(file_name, algorithm, num_filters):
    with open(file_name, "rb") as uncompressed:
        f = lzma.open(file_name + ".xz", "wb", format=algorithm, filters=num_filters)
        data = uncompressed.read(1024)
        while data:
            f.write(data)
            data = uncompressed.read(1024)
        f.close()

compress(filename, algorithm, num_filters)
print(filename + ".xz")
