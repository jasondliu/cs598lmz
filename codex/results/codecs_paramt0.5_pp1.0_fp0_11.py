import codecs
codecs.register_error("strict", codecs.ignore_errors)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",
                        help="path to input file",
                        type=str,
                        required=True)
    parser.add_argument("--output",
                        help="path to output file",
                        type=str,
                        required=True)
    parser.add_argument("--lang",
                        help="language to use",
                        type=str,
                        required=True)
    return parser.parse_args()

def main():
    args = parse_args()
    with open(args.input) as in_file, \
            codecs.open(args.output, "w", encoding="utf-8") as out_file:
        for line in in_file:
            line = line.strip()
            if line:
                tokens = tokenizer.tokenize(line, args.lang)
                for token in tokens:
                    out_file.write("{}\n".format(token))
                out_file.write("\
