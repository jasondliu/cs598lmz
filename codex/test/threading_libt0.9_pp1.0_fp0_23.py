import threading
threading._DummyThread._Thread__stop = lambda x: 42
threading._Timer._Thread__stop = lambda x: 42

config = configparser.ConfigParser()
config.read("config.ini")
def_country = config["Settings"]["Country"]
def_events = config["Settings"]["Events"]
def_banned_countries = [x.strip() for x in config["Settings"]["Banned Countries"].split(',')]
def_banned_event_names = [x.strip() for x in config["Settings"]["Banned Event Names"].split(',')]
debug = config["Settings"]["Debug"]
spreadsheet_id = config["Settings"]["Spreadsheet ID"]

driver = webdriver.Chrome()

class DeveloperNotifications(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        global message_content
        await self.client.wait_until_ready()
