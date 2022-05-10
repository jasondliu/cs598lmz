from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

def read_file(filename):
    with lzma.open('/media/sf_D_DRIVE/dsp_work/coding/python/data/data_0001.xz') as f:
        data = f.read()
        print(data)

if __name__ == "__main__":
    #read_file('/media/sf_D_DRIVE/dsp_work/coding/python/data/data_0001.xz')
    #print(sys.argv[1])
    read_file(sys.argv[1])
