import selectors
import sys
import types

class Process(object):

    def __init__(self, name, process_data, data_store):
        super(Process, self).__init__()
        self.name = name
        self.data_store = data_store
        self.process_data = process_data
        self.pid = None
        self.started = False
        self.stopped = False
        self.killed = False
        self.log = logging.getLogger(self.name)
        self._stdout = []
        self._stderr = []
        self.log_file = None

    def start(self):
        if self.started:
            raise RuntimeError("The process is already started")

        self.log.info("Starting process")
        self.log.info("Writing stdout and stderr to: %s", self.log_file)
        self.log.info("Executing: %s", " ".join(self.process_data['cmd']))

        self.proc = subprocess.Popen(self.process_data['cmd'
