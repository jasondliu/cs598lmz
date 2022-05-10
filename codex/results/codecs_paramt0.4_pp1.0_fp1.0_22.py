import codecs
codecs.register_error("strict", codecs.ignore_errors)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: " + sys.argv[0] + " <input> <output>")
        exit(0)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(input_file, 'r') as f:
        input_lines = f.readlines()

    with open(output_file, 'w') as f:
        for line in input_lines:
            line = line.strip()
            if line.startswith("#"):
                continue

            if "|" in line:
                line = line.split("|")[0]

            f.write(line + "\n")
