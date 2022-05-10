import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

previous = {}   # Dictionary with row_number as key and previous row as value
all_columns = {} # Dictionary with column name as key and index as value
ignored_columns = [] # List of columns that are ignored

def process_data(input_file, output_file):
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        reader = csv.reader(input_file, encoding='cp1252')
        writer = csv.writer(output_file)
        row_number = 0
        read_columns = False
        for row in reader:
            if row_number == 0:
                # Generate a mapping of column names in the input file to their index in this row
                print(row)
                global all_columns
                all_columns = dict(zip(row, range(0, len(row))))
                writer.writerow(row)   # Write
