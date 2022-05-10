import codecs
codecs.register_error('strict', codecs.ignore_errors)


class Line(object):

    def __init__(self, line_num, text):
        self.line_num = line_num
        self.text = text

    def __str__(self):
        return '{}: {}'.format(self.line_num, self.text)


def split_into_lines(big_str):
    return [Line(i, line) for i, line in enumerate(big_str.split('\n'), start=1)]


def strip_lines(lines):
    return [Line(line.line_num, line.text.strip())
            for line in lines]


def select_lines(lines, filter_func):
    return [line for line in lines if filter_func(line)]


def ignore_lines(lines, ignore_func):
    return [line for line in lines if not ignore_func(line)]


def parse_lines(lines, parser_func):
    return [parser_func(line) for line in lines]


def parse_author_lines(lines,
