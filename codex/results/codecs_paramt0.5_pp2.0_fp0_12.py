import codecs
codecs.register_error('strict', codecs.ignore_errors)

import csv
import re
import sys

def main(args):
    if len(args) < 2:
        print "Usage: %s <input file> [output file]" % args[0]
        return 1

    input_file = args[1]
    output_file = args[2] if len(args) >= 3 else None
    if output_file:
        output_file = open(output_file, 'w')
    else:
        output_file = sys.stdout

    reader = csv.reader(open(input_file))
    writer = csv.writer(output_file)
    for row in reader:
        if len(row) < 3:
            continue
        try:
            row[2] = unicode(row[2], 'utf-8')
        except UnicodeDecodeError:
            row[2] = unicode(row[2], 'iso-8859-1', 'strict')
        writer.writerow(row)

    return 0

if __name__ == '__
