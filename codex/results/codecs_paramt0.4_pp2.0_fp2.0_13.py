import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 {} <input_file> <output_file>".format(sys.argv[0]))
        exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with codecs.open(input_file, 'r', 'utf-8', 'strict') as fin:
        with codecs.open(output_file, 'w', 'utf-8') as fout:
            for line in fin:
                line = line.strip()
                if len(line) == 0:
                    continue
                tokens = line.split()
                new_line = []
                for token in tokens:
                    if len(token) == 0:
                        continue
                    if token[0] == "<":
                        new_line.append(token)
                        continue
                    if token[0] == "*":
                        new_line.append(token[1:])
                        continue

