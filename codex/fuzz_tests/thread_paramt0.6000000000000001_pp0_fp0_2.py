import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\r')).start()


class FIFOQueue(object):
    def __init__(self, max_size=None):
        self._max_size = max_size
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def push(self, item):
        if self._max_size is not None and len(self) > self._max_size:
            self._queue.pop(0)
        self._queue.append(item)

    def pop(self):
        return self._queue.pop(0)

    def __getitem__(self, idx):
        return self._queue[idx]

    def __iter__(self):
        return iter(self._queue)


class ReplayBuffer(object):
    def __init__(self, size, input_shape, n_actions, discrete=False):
        self.mem_size = size
        self.mem_cntr = 0
        self.discrete = discrete
        self.state_memory = np.zer
