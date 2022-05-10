import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
# Enable logging
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Connecting to the database file
try:
    engine = sq.create_engine('sqlite:///main.db')
except BaseException as e:
    logger.error("Invalid file path. db error: {}".format(e))

# Creating a database session
Session = sq.orm.sessionmaker(bind=engine)
session = Session()

# Getting own Id
bot = telegram.Bot(token=token)
bot_name = bot.get_me().username


# Checking for private messages
def private(update, context):
    # If recieved message is /start
    if update.message.text == "/start":
        update.message.reply_text(start_text)

