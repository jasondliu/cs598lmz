import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def _parse_args():
    parser = argparse.ArgumentParser(description='Postprocess the crawled data')

    parser.add_argument('--data-dir', dest='data_dir', type=str,
                        default=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data'),
                        help='the directory to store crawled data')

    parser.add_argument('--k-core', dest='core_num', type=int,
                        default=0,
                        help='the number of K-core')

    parser.add_argument('--group-num', dest='group_num', type=int,
                        default=10,
                        help='the number of groups in each K-core')

    parser.add_argument('--sample-num', dest='sample_num', type=int,
                        default=10,
                        help='the number of samples in each group')

    return parser.parse_args()

class
