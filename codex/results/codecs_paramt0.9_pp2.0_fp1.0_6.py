import codecs
codecs.register_error('strict', codecs.ignore_errors)


PREFIX = os.path.dirname(os.path.abspath(sys.argv[0]))+'/data/'

def main():
    for arguments in iter(sys.stdin.readline, ''):
        (sentence, source) = arguments.split('\t')
        (sentence, source) = (sentence.strip(), source.strip())
        lst = []
        if len(lst) == 0:
            print sentence, '<===>', source, '<===>', sentence

if __name__ == "__main__":
    main()
