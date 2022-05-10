import codecs
codecs.register_error("strict", codecs.ignore_errors)

def unicode_to_ascii(s):
    #return s.encode("ascii", "ignore")
    return s.encode("utf-8", "ignore")

def read_file(filename):
    f = codecs.open(filename, "rb", "utf-8")
    lines = f.readlines()
    f.close()
    return lines

def write_file(filename, lines):
    f = codecs.open(filename, "wb", "utf-8")
    f.writelines(lines)
    f.close()

def read_csv(filename):
    lines = read_file(filename)
    rows = []
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        row = line.split(",")
        rows.append(row)
    return rows

def write_csv(filename, rows):
    lines = []
    for row in rows:
        line = ",".join(row)
        lines
