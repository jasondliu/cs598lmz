import lzma
# Test LZMADecompressor

def main():
    with open('data/sample.xz', 'rb') as f:
        with lzma.open(f, 'rb') as xz_file:
            file_content = xz_file.read()
            print(file_content)

