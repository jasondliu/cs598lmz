import gc, weakref
from vertigo.loop import * # EventLoop
from vertigo.debug import * # Logger

class Vertigo(object):

    def __init__(self, nthreads=3):
        self.lock = threading.Lock()

        if nthreads<1: nthreads=1
        self.done=False;
        self.nthreads=nthreads
        self.threads=[]

        if nthreads>=1:
            self.loop=EventLoop()
            self.threads.append( threading.Thread(target=self.loop.run) )
        for i in range(1,nthreads):
            self.threads.append( threading.Thread(target=self.run, args=[i]) )


    def run(self,i):
        loop=EventLoop()
        while not self.done:
            try: loop.dispatchAll()
            except Exception as e:
                #emit(Error,self,e)
                raise

    def start(self):
        for th in self.threads: th.start()
