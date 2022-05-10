import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Configure logging.
#

logging.basicConfig(format='%(asctime)-15s %(levelname)-6s %(threadName)-12s %(message)s',
                    level=logging.INFO)

# The main loop.
#

if __name__ == '__main__':

    # Get the application object.
    #
    try:
        app = QApplication(sys.argv)

        # Make sure that we are using QT5.
        #
        if not QT_VERSION_STR.startswith('5'):
            raise Exception('Qt5 required')

        # Create the main window.
        #
        window = PAMWindow()
        window.show()

        # Start the event loop.
        #
        rc = app.exec_()

    except Exception as e:
        logging.exception(e)
        rc = 1
    else:
        rc = 0
    sys.exit(rc)
