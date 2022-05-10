import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# ---------- Variables ----------

DATABASE_URL = os.environ['DATABASE_URL']

# ---------- Methods ----------


# Create a logging object
def create_logger():
    logger = logging.getLogger("check_red_flags")
    logger.setLevel(logging.DEBUG)

    # create the logging file handler
    logFile = 'check_red_flags.log'

    fh = logging.FileHandler(logFile)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(fh)
    return logger


# Get the oldest 100 flags that are new
def get_new_flags(logger):
    conn = psycopg2.connect(DATABASE_URL)
   
