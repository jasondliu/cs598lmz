import codecs
codecs.register_error('ignore_space', codecs.lookup_error('ignore'))

def read_csv(file_name):
    """
    Reads the CSV file in file_name to a Pandas DataFrame.
    """
    return pd.read_csv(file_name)

def read_csv_to_list(file_name):
    """
    Reads the CSV file in file_name to a list of lists.
    """
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
    return csv_list

def read_csv_to_dict(file_name):
    """
    Reads the CSV file in file_name to a dictionary of dictionaries.
    """
    with open(file_name, 'r') as f:
        reader = csv.DictReader(f)
        csv_dict = {}
        for row in reader:
            csv_dict[row['id']] = row
    return csv_dict

def write_csv
