import lzma
# Test LZMADecompressor
bytes_io = io.BytesIO(compress(b'Hello world!'))

# Open as xz file
with lzma.open(fileobj=bytes_io) as lzma_file:
    try:
        lzma_file.read()
    except IOError as err:
        print('IOError: %s' % err)
    except OSError as err:
        print('OSError: %s' % err)
    except:
        print('unexpected error:', sys.exc_info()[0])
        raise
    

# Open directly with lzma.LZMAFile
with lzma.LZMAFile(fileobj=bytes_io) as lzma_file:
    try:
        lzma_file.read()
    except IOError as err:
        print('IOError: %s' % err)
    except OSError as err:
        print('OSError: %s' % err)
    except:
        print('unexpected error:', sys.exc_info()[0])
        raise
