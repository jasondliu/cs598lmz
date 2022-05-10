import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def __enter__(self):
        self.f = open(self.name, "rb")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

from pprint import pprint
from collections import Counter

def main():
    arguments = docopt(__doc__, version='1.0')
    input_index = arguments["<input_index>"]
    output_index = arguments["<output_index>"]
    index_name = arguments["<index_name>"]
    # id_convert_file = arguments["<id_convert_file>"]
    try:
        with gzip.open(input_index, "rb") as in_stream:
            with File(output_index) as out_stream:
                field_names = list()
                for line in in_stream:
                    line_str = line.decode('utf
