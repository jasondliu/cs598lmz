import codecs
codecs.register_error('strict', codecs.ignore_errors)

get_write = lambda writer: lambda row: writer.writerow(row)

def read_csv(infilename, dialect='excel', **kwargs):
    with open(infilename, 'rb') as infile:
        reader = csv.reader(infile, dialect=dialect, **kwargs)
        for row in reader:
            yield row

def read_all_csv(infilename, dialect='excel', **kwargs):
    data = []
    with open(infilename, 'rb') as infile:
        reader = csv.reader(infile, dialect=dialect, **kwargs)
        for row in reader:
            data.append(row)
    return data


def write_csv(outfilename, dialect='excel', encoding='ascii', **kwargs):
    with open(outfilename, 'wb') as outfile:
        writer = csv.writer(outfile, dialect=dialect, **kwargs)
        write = get_write(writer)
        return write


def write
