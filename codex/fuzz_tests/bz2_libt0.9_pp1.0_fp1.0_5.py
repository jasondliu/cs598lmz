import bz2
bz2.cbufsize = 16 * 1024 # this is important, otherwise will get 
                         # EOFError: Compressed file ended before the end-of-stream marker was reached
                         # from https://stackoverflow.com/a/56776383/1381447

def is_valid_bz2(file_name):
    """Return true iff the given file is a valid bz2 file '"""
    err = ''
    if not file_name.lower().endswith('.bz2'):
        return False
    if not os.path.exists(file_name):
        return False
    try:
        with open(file_name, 'r') as bz_file:
            test_line = bz_file.readline()
            bz2.decompress(test_line)
            return True
    except IOError as err:
        logging.error('[%s] is not a bz2 file (IOError): %s', file_name, str(err))
        return False
    except:
        logging.error('[%s] is
