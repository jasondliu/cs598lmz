from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\x00')

if __name__ == '__main__':
    print('Process (%s) start...' % os.getpid())
    for i in range(5):
        p = Process(target=run_proc, args=('test',))
        print('Child process will start.')
        p.start()
    p.join()
    print('Child process end.')
