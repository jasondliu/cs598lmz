import codecs
# Test codecs.register_error('replace_with_space', codecs.replace_with_space)
# codecs.register_error('replace_with_space', codecs.replace_with_space)


def read_file(file_name):
    f = codecs.open(file_name, "r", "utf-8")
    lines = f.readlines()
    f.close()
    return lines


def write_file(file_name, lines):
    f = codecs.open(file_name, "w", "utf-8")
    f.writelines(lines)
    f.close()


def main():
    lines = read_file("../data/data.txt")
    print(lines)
    write_file("../data/data_copy.txt", lines)


