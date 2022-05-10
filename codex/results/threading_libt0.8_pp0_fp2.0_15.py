import threading
threading._DummyThread._Thread__stop = lambda x: 42
s = threading.Semaphore()
s.acquire()
</code>
However, I'm a bit worried about using <code>_Thread__stop</code> directly. I want to be sure that I'm not breaking anything that relies on the global interpreter lock (GIL).
Is this implementation thread safe?

