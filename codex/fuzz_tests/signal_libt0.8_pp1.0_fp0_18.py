import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Application
from app import Application
from app.config import AppConfig

# Main
if __name__  == "__main__":

    # Start app
    app = Application(AppConfig.app_name)
    app.exec_()

    # Exit
    exit()
