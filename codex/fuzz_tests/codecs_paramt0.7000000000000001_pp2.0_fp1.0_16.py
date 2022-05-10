import codecs
codecs.register_error('strict', codecs.ignore_errors)

import sys

class TextFileParser(object):
    def __init__(self, delimiter=None, encoding=None, ignore_lines=0, out_name=None,
                 format=True, update=False, get_format=False, out_type=False):
        self.delimiter = delimiter
        self.encoding = encoding
        self.ignore_lines = ignore_lines
        self.out_name = out_name
        self.format = format
        self.update = update
        self.get_format = get_format
        self.out_type = out_type

    def get_combined_format(self, format_list):
        combined_format = {}
        for format_dict in format_list:
            for key in format_dict:
                if key in combined_format:
                    if format_dict[key] > combined_format[key]:
                        combined_format[key] = format_dict[key]
                else:
                    combined_format[key] = format_dict[key]
       
