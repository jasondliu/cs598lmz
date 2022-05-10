import codecs
codecs.register_error('strict', codecs.ignore_errors)
sys.stdout = codecs.getwriter('ascii')(sys.stdout, 'strict')

def read_input(file):
    for line in file:
        yield line.split()

input_file = read_input(sys.stdin)
mapper_out = []

for words in input_file:
    mapper_out.extend(words)

for word in mapper_out:
    print '%s\t%s' % (word, 1)
