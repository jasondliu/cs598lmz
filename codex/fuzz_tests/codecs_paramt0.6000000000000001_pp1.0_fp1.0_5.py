import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--tgt-lang', required=True, help="target language")
    parser.add_argument('-s', '--src-lang', required=True, help="source language")
    parser.add_argument('-i', '--input', required=True, help="input file")
    parser.add_argument('-o', '--output', required=True, help="output file")
    parser.add_argument('--src-vocab', help="source language vocabulary")
    parser.add_argument('--tgt-vocab', help="target language vocabulary")
    #parser.add_argument('-p', '--processes', type=int, default=1,
    #                    help="number of processes to use")
    parser.add_argument('--len-ratio', type=float, default=0.7,
                        help="maximum ratio between source and target lengths")
    parser.add_argument('--shard-size',
