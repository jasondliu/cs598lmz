import threading
threading.StackSize(1500000000)

################################################################################
# Current Execution Process

class run_current_process_in_a_thread(threading.Thread):
    def __init__(self,p):
        threading.Thread.__init__(self)
        self.process = p
        self.completed_process = None
        self.process_exception = None

    def run(self):
        cwd = os.getcwd()
        try:
            self.completed_process = subprocess.run(
                self.process, universal_newlines=True, check=True)
        except Exception as e:
            print("{}\n{}".format(e,self.process), flush=True)
            self.process_exception = e
            raise e

def run(p):
    p.run()
    return p
