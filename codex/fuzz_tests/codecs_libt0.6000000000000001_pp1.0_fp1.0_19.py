import codecs
codecs.getwriter('utf-8')(sys.stdout)

def main(args):
    if len(args) < 3:
        print "Usage: python %s <input-file> <output-file>" % args[0]
        exit(1)
    input_file = args[1]
    output_file = args[2]

    f = codecs.open(input_file, 'r', 'utf-8')
    lines = f.readlines()
    f.close()

    f = codecs.open(output_file, 'w', 'utf-8')
    for line in lines:
        line = line.strip()
        if line != "":
            word = line.split(" ")[0]
            f.write(word + "\n")
    f.close()

if __name__ == '__main__':
    main(sys.argv)
