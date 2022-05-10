import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

def main(argv):
    if len(argv) != 2:
        print('argv error!')
        exit(-1)
    fname = argv[1]
    fpath = os.path.abspath(fname)
    print('fname: ', fname)
    print('fpath: ', fpath)
    if not os.path.exists(fpath):
        print('file not found: ', fpath)
        exit(-2)
    if fname.endswith('.csv'):
        processCSV(fpath)
    elif fname.endswith('.csvx'):
        processCSVX(fpath)
    elif fname.endswith('.v'):
        processVerilog(fpath)
    else:
        print('unknown file: ', fname)
        exit(-3)


def processCSV(fpath):
    # load CSV
    print('
