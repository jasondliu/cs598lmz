import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser(description='Extracts the features for the given dataset.')
    parser.add_argument('dataset', type=str, help='The dataset to extract features from.')
    parser.add_argument('--output', type=str, help='The output file to write to.')
    args = parser.parse_args()

    # Load the dataset
    print 'Loading dataset...'
    dataset = Dataset(args.dataset)
    print 'Loaded dataset.'

    # Extract the features
    print 'Extracting features...'
    features = extract_features(dataset)
    print 'Extracted features.'

    # Write the features to a file
    if args.output:
        print 'Writing to file...'
        with open(args.output, 'w') as f:
            f.write(json.dumps(features))
        print 'Wrote to file.'

def extract_features(dataset):
    features = []
    for i in
