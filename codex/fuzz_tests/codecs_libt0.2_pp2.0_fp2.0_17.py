import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set up the argument parser
parser = argparse.ArgumentParser(description='Run the bot')
parser.add_argument('--config', help='The config file to use', default='config.json')
parser.add_argument('--debug', help='Run in debug mode', action='store_true')
parser.add_argument('--no-loop', help='Do not run the bot in a loop', action='store_true')

# Parse the arguments
args = parser.parse_args()

# Load the config
with open(args.config, 'r') as f:
    config = json.load(f)

# Set up the bot
bot = Bot(config)

# Run the bot
if args.debug:
    bot.run()
else:
    while True:
        try:
            bot.
