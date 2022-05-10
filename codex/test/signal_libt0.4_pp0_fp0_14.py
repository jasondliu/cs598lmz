import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("http://www.google.com")

# the page is ajaxy so the title is originally this:
