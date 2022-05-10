import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
