import codecs
codecs.register_error('strict', codecs.ignore_errors)


def file_to_iter(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as inf:
            for line in inf:
                yield line
    except UnicodeDecodeError:
        # you should be able to use codecs.open and specify a read handler
        with open(filename, 'r', encoding='ascii', errors='strict') as inf:
            for line in inf:
                yield line


def file_to_lines(filename):
    return [line.strip() for line in file_to_iter(filename)]


def file_to_lines_as_string(filename):
    return '\n'.join(line for line in file_to_iter(filename))


def file_to_sorted_unique_lines(filename):
    return sorted(dict(line=True for line in file_to_iter(filename)).keys())


def file_to_words(filename):
    for line in file_to_iter(filename):
        for word in splitter(line):
