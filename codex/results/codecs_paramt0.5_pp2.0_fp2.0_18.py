import codecs
codecs.register_error('ignore', codecs.lookup('utf-8'))

def main():
    # Input parameters
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Path to input file', required=True)
    parser.add_argument('-o', '--output', help='Path to output file', required=True)
    args = parser.parse_args()

    # Create output directory if it doesn't exist
    out_dir = os.path.dirname(args.output)
    if out_dir != '' and not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # Read data
    data = pd.read_csv(args.input, encoding='utf-8')

    # Filter data
    data = data[data.lang == 'en']
    data = data[data.retweeted_status.isnull()]
    data = data[data.in_reply_to_status_id.isnull()]
    data = data[data.in_reply_to_
