import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Convert a .csv file to a .json file')
    parser.add_argument('-i', '--input', help='Input .csv file', required=True)
    parser.add_argument('-o', '--output', help='Output .json file', required=True)
    args = parser.parse_args()

    with codecs.open(args.input, 'r', 'utf-8', 'strict') as f:
        reader = csv.reader(f)
        headers = next(reader)
        data = [dict(zip(headers, row)) for row in reader]

    with codecs.open(args.output, 'w', 'utf-8', 'strict') as f:
        json.dump(data, f, ensure_ascii=False)

if __name__ == '__main__':
    main()
