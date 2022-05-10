import threading
threading.stack_size(67108864) # 64MB stack

# The class is our Flamenco Manager instance
class FlamencoManager(threading.Thread):
    def __init__(self):
        super(FlamencoManager, self).__init__()

    def run(self):
        """ Main code for the runnin Manager"""
        print("Starting Flamenco Manager ...")
        self.flamencoManager = FlamencoManagerAPIClient()
        if not self.flamencoManager.is_connected():
            self.flamencoManager.connect()

        self.flamencoManager.create_job_types()
        self.flamencoManager.create_job()

        # Run the server forever
        self.flamencoManager.run()


main_thread = FlamencoManager()
main_thread.start()
