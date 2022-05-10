import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  Functions
#
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#
#  Main program
#
#------------------------------------------------------------------------------

# Load configuration
config = ConfigParser.ConfigParser()
config.read('myt.cfg')

# Set up logging
logging.basicConfig(filename=config.get('logging', 'filename'),
                    level=config.get('logging', 'level'),
                    format=config.get('logging', 'format', 1))

# Connect to database
db = MySQLdb.connect(host=config.get('database', 'host'),
                     user=config.get('database', 'user'),
                     passwd=config.get('database', 'password'),
                     db=config.get('database', 'name'))

# Get the data
cursor = db.cursor()
cursor.execute("""SELECT id, name, description,
                  DATE_FORMAT(start_date, '%%Y-%%m-%%d %%H:%%i:%%s'),
                  DATE_FORM
