import codecs
codecs.register_error("strict", codecs.ignore_errors)

def read_csv(filename):
    """
    Read a CSV file into a list of rows.
    """
    with open(filename, "rb") as f:
        reader = csv.reader(f)
        return list(reader)

def write_csv(rows, filename):
    """
    Write a list of rows to a CSV file.
    """
    with open(filename, "wb") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

def read_tsv(filename):
    """
    Read a TSV file into a list of rows.
    """
    with open(filename, "rb") as f:
        reader = csv.reader(f, delimiter="\t")
        return list(reader)

def write_tsv(rows, filename):
    """
    Write a list of rows to a TSV file.
    """
    with open(filename, "wb") as f:
        writer = csv.writer
