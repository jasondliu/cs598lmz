import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\n')).start()

class State(enum.Enum):
    UNKNOWN = 0
    SUCCESS = 1
    FAIL = 2

class StatusCode(enum.Enum):
    UNKNOWN = 0
    OK = 1
    FAIL = 2

class Result:
    def __init__(self, state, status_code, msg):
        self.state = state
        self.status_code = status_code
        self.msg = msg

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'Result[state={}, status_code={}, msg={}]'.format(self.state, self.status_code, self.msg)

class ResultBuilder:
    def __init__(self, state, status_code, msg):
        self.state = state
        self.status_code = status_code
        self.msg = msg

    def build(self):
        return Result(self.state, self.status_code, self.msg)

