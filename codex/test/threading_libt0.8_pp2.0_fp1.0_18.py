import threading
threading.stack_size(1024*1024*8)

class SumThread(threading.Thread):
    def __init__(self, numbers):
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.result = 0

    def run(self):
        self.result = sum(self.numbers)

def main():
    nums = [i for i in range(10000000)]
    num_threads = 4
    threads = []
    for i in range(num_threads):
        start_pos = int(i * len(nums) / num_threads)
        end_pos = int((i+1) * len(nums) / num_threads)
        thread = SumThread(nums[start_pos:end_pos])
        threads.append(thread)

    start = time.time()
    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print('sum=%d' % sum([t.result for t in threads]))
    end
