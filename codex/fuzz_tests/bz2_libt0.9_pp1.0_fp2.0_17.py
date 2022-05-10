import bz2
bz2.PY3

open('/tmp/file', 'w').write('''\
line 1
  line 2   

    line 3
''')

import re
wordPat = re.compile(r'\w+')
def openOne(path):
    print(line)
    showmatch(wordPat.search('Once upon a time'))

def showmatch(match):
    if match is None:
        print('no match')
    else:
        print(match)
if __name__ == '__main__':
    import fileinput
    print('='*20)
    print('FILE\t\t\tLINENO\t\tLINE')
    print('='*20)
    for line in fileinput.input('/tmp/file'):
        print("%-16s %-4d %-s" % (fileinput.filename(), fileinput.filelineno(), fileinput.lineno()), end='')
        openOne(fileinput.filename())
    if fileinput.isstdin():
        print('[stdin]')
import
