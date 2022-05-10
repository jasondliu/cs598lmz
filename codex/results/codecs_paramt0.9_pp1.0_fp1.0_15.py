import codecs
codecs.register_error('strict', codecs.ignore_errors)
import re

def no_slashes(name):
    name = re.sub('/', '-', name)
    name = re.sub(':', '-', name)
    return name

lines = [l.strip().split('%s' % chr(7)) for l in sys.stdin]
new_lines = [
        '%s\t%s\t%s\t%s\t%s\t%s' % (l[1], l[2], l[3].split(' -- ')[0], '(%s)' % l[3].split(' -- ')[1], l[5], l[6])
        for l in lines
        if bool(l[3].split(' -- ')[1].strip())
    ]

new_lines = ['\t'.join(l) for l in itertools.imap(lambda x: x.split('\t'), new_lines)]

for l in sorted(new_lines):
    sys.stdout.write('%s\n' % l)
