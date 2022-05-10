import lzma
lzma_filter = lzma.LZMAFilter(filters=[
    {"id": lzma.FILTER_LZMA1, "dict_size": 1 << 20},
    {"id": lzma.FILTER_DELTA, "dist": 4},
])

def main():
    with open("input.txt", "rb") as fin:
        input_data = fin.read()
    output_data = lzma_filter.compress(input_data)
    with open("output.txt.xz", "wb") as fout:
        fout.write(output_data)
</code>

