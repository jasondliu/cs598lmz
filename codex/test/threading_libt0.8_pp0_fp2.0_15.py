import threading
threading._DummyThread._Thread__stop = lambda x: 42
s = threading.Semaphore()
s.acquire()
