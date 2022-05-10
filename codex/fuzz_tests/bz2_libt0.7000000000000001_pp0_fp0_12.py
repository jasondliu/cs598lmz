import bz2
bz2.BZ2File.MIN_IO_SIZE = 1

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', type=str, required=True)
    parser.add_argument('--output-file', type=str, required=True)
    parser.add_argument('--num-workers', type=int, required=True)
    parser.add_argument('--num-samples', type=int, required=True)
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--input-format', type=str, default='tsv')
    args = parser.parse_args(argv)

    random = np.random.RandomState(args.seed)
    pool = multiprocessing.Pool(args.num_workers)
    try:
        with open(args.output_file, 'w') as f:
            for samples in pool.imap(
                SampleLine,
                pool.imap(
                    lambda i: (i, args
