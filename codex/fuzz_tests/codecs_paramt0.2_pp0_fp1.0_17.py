import codecs
codecs.register_error('strict', codecs.ignore_errors)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', required=True, help='input file')
    parser.add_argument('--output', '-o', required=True, help='output file')
    parser.add_argument('--vocab', '-v', required=True, help='vocab file')
    parser.add_argument('--unk', '-u', default='<unk>', help='unknown token')
    parser.add_argument('--eos', '-e', default='<eos>', help='end-of-sentence token')
    parser.add_argument('--bos', '-b', default='<bos>', help='beginning-of-sentence token')
    parser.add_argument('--pad', '-p', default='<pad>', help='padding token')
    parser.add_argument('--limit', '-l', type=int, help='limit vocab size')
    args = parser.parse_args()

   
