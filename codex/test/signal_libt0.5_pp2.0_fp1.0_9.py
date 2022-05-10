import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# initialize the logger
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--config', help='the configuration file')
parser.add_argument('--log', help='the log level')
args = parser.parse_args()

if args.log:
    logger.setLevel(args.log.upper())

# read the configuration file
if args.config:
    config = configparser.ConfigParser()
    config.read(args.config)
else:
    config = configparser.ConfigParser()
    config.read('config.ini')

# initialize the database
db = Database(config['DATABASE']['path'], logger)

# initialize the API
api = API(config['API'], logger)


