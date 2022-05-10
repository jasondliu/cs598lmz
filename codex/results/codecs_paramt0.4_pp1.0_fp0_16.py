import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    for line in sys.stdin:
        try:
            line = line.decode('utf-8', 'strict')
        except UnicodeDecodeError:
            continue
        print line.encode('utf-8')

if __name__ == '__main__':
    main()
