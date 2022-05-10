import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# Setup logging to monitor the program
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

# Read configuration from config file
config = configparser.ConfigParser()
config.read('config.ini')

# Create global variables
credentials = []
cmd_sched = ""
cmd_temp = ""
cmd_convert = ""

# Create global variables for MySQL
mysql_conn = None
mysql_cursor = None


def main():
    """
    Main function to run the program
    """
    # Start the MySQL connection
    mysql_connect()

    # Get the command line arguments
    args = get_args()

    # Check if the arguments
