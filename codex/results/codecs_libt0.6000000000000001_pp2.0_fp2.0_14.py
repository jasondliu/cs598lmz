import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input_csv', help='Input CSV file', required=True)
    parser.add_argument('-o', '--output_csv', help='Output CSV file', required=True)
    parser.add_argument('-c', '--countries_csv', help='Countries CSV file', required=True)
    parser.add_argument('-l', '--country_level', help='Country level', required=True)
    args = parser.parse_args()
    return args

def main():
    args = get_args()

    countries = {}
    # Read countries CSV file
    with open(args.countries_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            countries[row['country']] = row['latitude'] + ',' + row['
