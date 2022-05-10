import bz2
# Test BZ2Decompressor class

def main():
    decompressor = bz2.BZ2Decompressor()
    with open('lorem.txt.bz2', 'rb') as input, open('uncompressed.txt', 'w') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            print(data)
            # data that gets stored in text is not output to the console
            out_data = decompressor.decompress(data)
            if out_data:
                output.write(out_data.decode('utf-8'))
                print(out_data)

if __name__ == '__main__':
    main()
