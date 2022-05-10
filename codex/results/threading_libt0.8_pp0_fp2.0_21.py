import threading
threading.Thread.daemon = True

# UserInterface.py
class UserInterfaceController(object):
    def __init__(self):
        self.file_count = 0

    def start(self):
        # q = Queue.Queue()
        # ui = UI.UserInterface_t(q)
        self.t1 = threading.Thread(target=self.user_interface)
        self.t1.daemon = True
        self.t1.start()

    def user_interface(self):
        q = Queue.Queue()
        ui = UI.UserInterface_t(q)
        ui.start()
        while True:
            msg = q.get()
            if msg == 'get_status_update':
                # msg = 'User Interface status update'
                ui.ui_status_update(self.file_count)
                q.task_done()
            elif msg == 'get_file_count':
                # msg = 'User Interface file count'
                ui.ui_file_count(self.file_count)
               
