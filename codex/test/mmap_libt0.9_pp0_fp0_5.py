import mmap


def iterate_csv(file_name):
    try:
        with open(file_name) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                yield row
    except IOError:
        print('Could not open file: ', file_name)


