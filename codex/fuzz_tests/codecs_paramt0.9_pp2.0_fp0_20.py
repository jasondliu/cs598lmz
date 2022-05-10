import codecs
codecs.register_error('strict', codecs.lookup('UTF8'))

def guess_file_encoding(fname):
    with open(fname, 'rb') as fh:
        fcontent = fh.read()
        prev = None
        possible_encodings = [
            'utf-8',
            'latin-1',
            'windows-1252',
            'utf-16',
            'cp437',
        ]
        for enc in possible_encodings:
            try:
                fcontent.decode(enc, 'strict')
                if enc != prev:
                    print('Using encoding: %s for file: %s' % (enc, fname))
                break
            except Exception as e:
                prev = enc
        else:
            raise

if __name__ == '__main__':
    guess_file_encoding(sys.argv[1])
