import bz2
# Test BZ2Decompressor
with bz2.BZ2File('./data/sample.txt.bz2') as binary_file:
    with io.BufferedReader(binary_file) as buffered_file:
        with TextIOWrapper(buffered_file, encoding='utf-8') as text_file:
            for line in text_file:
                print(line)

print("-" * 40)

# Test BZ2File
with BZ2File('./data/sample.txt.bz2') as text_file:
    for line in text_file:
        print(line)
