import codecs
codecs.register_error('strict', codecs.ignore_errors)


#
# Returns a dictionary containing data from the CSV file.
# Key is the column name, value is a list of the data in that column.
#
def read_csv(filename):
    with codecs.open(filename, 'r', encoding='utf-8',
                     errors='strict') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
        data = {}
        for column_name in header:
            data[column_name] = []
        for row in reader:
            for (index, value) in enumerate(row):
                data[header[index]].append(value)
    return data


#
# Replaces the field with the value.
#
def replace_field(data, field, replacement_field, value):
    data[replacement_field] = []
    for datum in data[field]:
        if datum == value:
            data[replacement_field].append(1)
        else:
            data[replacement_field].
