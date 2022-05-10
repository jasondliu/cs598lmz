import threading
threading.stack_size(1000000)

class Master:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.num_threads = 0
        self.data = []
        self.threads = []
        self.results = []
        self.output = []
        self.start_time = 0
        self.end_time = 0
        self.total_time = 0
        self.file_name = 'output.txt'

    def read_input(self):
        self.width, self.height, self.num_threads = map(int, raw_input().split())
        self.data = [0] * self.height
        for i in range(self.height):
            self.data[i] = map(int, raw_input().split())

    def init_threads(self):
        self.threads = []
