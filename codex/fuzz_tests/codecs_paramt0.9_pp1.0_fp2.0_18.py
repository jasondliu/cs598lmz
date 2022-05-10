import codecs
codecs.register_error("strict", codecs.ignore_errors)

def convert(withFilename, character='y', surrogate='\uFFFD'):
    number = 0
    def convertYears(match):
        nonlocal number
        newChar, number = chr(ord(character) + number), number + 1
        return character + match.group(2) + newChar

    with open(withFilename, mode='r', encoding='strict') as withFile:
        for line in withFile:
            yearLine = re.sub('(^\d{4})-(\d{2})', convertYears, line, count=1)
            if yearLine:
                print(yearLine, end='')

# -------------------------------------------------------------------
# Python 3 main
# -------------------------------------------------------------------
if __name__ == '__main__':
    convert(sys.argv[1])
