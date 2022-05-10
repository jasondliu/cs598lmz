import threading
# Test threading daemon
import queue

Q = queue.Queue()


class Producer(threading.Thread):
    def run(self):
        for i in range(10):
            Q.put(i)
        print("Producer notify : product done")


class Consumer(threading.Thread):
    def run(self):
        while True:
            product = Q.get()
            print("Consumer notify : product consumed %s" % product)


def main():
    producer = Producer()
    consumer = Consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()


if __name__ == '__main__':
    main()
