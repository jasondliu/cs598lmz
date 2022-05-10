import threading
threading.stack_size(2**27)
#sys.setrecursionlimit(10**7)

class Solver:
    def __init__(self, s):
        self.N = len(s)
        self.s = s
        self.t = ''
        self.i = 0
        self.ans = ''
        self.low_index_stack = []
        self.memo_index_stack = []

        if self.N % 2 == 0:
            self.part_size = self.N // 2
        else:
            self.part_size = self.N // 2 + 1
        self.max_part_size = self.N // 2 + 1

    def search_min(self):
        print(self.N)
        self.t = self.s[:self.part_size]
        #print(self.t)
