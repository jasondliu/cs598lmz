import codecs
codecs.register_error("strict", codecs.ignore_errors)

#
# The following function is used to read in a file and return a list of
# lines, removing comments and blank lines.
#
def read_file(filename):
    lines = []
    for line in codecs.open(filename, "r", "utf-8", "strict"):
        line = line.strip()
        if line == "" or line[0] == "#":
            continue
        lines.append(line)
    return lines

#
# The following function is used to write out a file, given a list of lines.
#
def write_file(filename, lines):
    file = codecs.open(filename, "w", "utf-8", "strict")
    for line in lines:
        file.write(line)
        file.write("\n")
    file.close()

#
# The following function is used to read in a file and return a list of
# lines, removing comments and blank lines.
#
def read_file_as_string(filename):
    lines = read_file
