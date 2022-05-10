import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# The following functions are used to convert the data from the
# original format to the format used in this project.
#

def convert_to_csv(input_file, output_file):
    """
    Convert the input file to a CSV file.
    """
    with open(input_file, 'r') as in_file:
        with open(output_file, 'w') as out_file:
            writer = csv.writer(out_file)
            for row in csv.reader(in_file):
                if len(row) == 3:
                    writer.writerow(row)

def convert_to_unicode(input_file, output_file):
    """
    Convert the input file to a Unicode file.
    """
    with codecs.open(input_file, 'r', encoding='utf-8', errors='strict') as in_file:
        with codecs.open(output_file, 'w', encoding='utf-8', errors='strict') as out_file:
            for line
