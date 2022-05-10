import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Load the KV lang file
Builder.load_file('main.kv')

# Declare the main widget class
class MainWidget(Widget):
    # Declare the class variables
    DATAPATH = "data/data.csv"
    DATAPATH_LAST_ROW = "data/last_row.csv"
    devicename = "Test"
    data = []
    data_last_row = []
    labels = ["Time", "Temperature", "Pressure", "Battery"]
    store_interval = 60 # seconds
    store_interval_id = 0
    start_time = 0

    # Constructor
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.initialize()

    # Initialization method
    def initialize(self):
        # Set the start time of the app
        self.start_time = time.time()

        # Set the device name
