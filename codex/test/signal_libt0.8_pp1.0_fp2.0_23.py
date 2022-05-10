import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Download and unzip the data
if not os.path.isdir(DATA_DIR):
    os.makedirs(DATA_DIR)
if not os.path.isfile(os.path.join(DATA_DIR, "hs.zip")):
    os.system('wget -P ' + DATA_DIR + ' ' + DATA_URL)
    os.system('unzip hs.zip -d ' + DATA_DIR)
