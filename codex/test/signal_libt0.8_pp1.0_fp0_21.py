import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Parse command line arguments
parser = argparse.ArgumentParser(description='Plot navigation data.')
parser.add_argument('datadirs', metavar='datadir', nargs='+', help='Data directories')
parser.add_argument('--nogps', default=False, action='store_true', help='Do not plot GPS track')
parser.add_argument('--nopoiseat', default=False, action='store_true', help='Do not plot poiseat position estimates')
parser.add_argument('--noins', default=False, action='store_true', help='Do not plot INS position estimates')
parser.add_argument('--nofiltered', default=False, action='store_true', help='Do not plot filtered position estimates')
parser.add_argument('--nodelta', default=False, action='store_true', help='Do not plot delta position estimates')
