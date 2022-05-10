import codecs
codecs.register_error('strict', codecs.ignore_errors)

DYK_TEMPLATE_RE = re.compile(r'\{\{[Dd]id you know nominations/\d\d\d\d\d\d\d\d\d\d\d')

def main():
    for line in fileinput.input():
        if DYK_TEMPLATE_RE.search(line):
            print(codecs.decode(line, 'utf-8', 'strict'))

if __name__ == '__main__':
    main()
