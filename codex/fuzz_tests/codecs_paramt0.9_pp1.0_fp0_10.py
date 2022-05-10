import codecs
codecs.register_error('replace_with_space', codecs.replace_with_spaces)

def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with codecs.open(input_file, 'r', encoding='utf-8',
                     errors='replace_with_spaces') as f, \
        open(output_file, 'w') as o:

        for line in f:
            o.write(line)

if __name__ == '__main__':
    main()
