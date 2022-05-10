import threading
# Test threading daemon mode
#
# @author Yannick Jestin <jestin@cena.fr>
#
# (c) CENA
#
# This code is licenced under the GPL
#

class TestThread(threading.Thread):
  def __init__(self,name):
    threading.Thread.__init__(self)
    self.name=name
    self.daemon=True
  def run(self):
    print "Thread %s started"%self.name
    for i in range(0,10):
      print "Thread %s running"%self.name
      time.sleep(1)
    print "Thread %s terminated"%self.name


if __name__=="__main__":
  t1=TestThread("1")
  t2=TestThread("2")
  t1.start()
  t2.start()
  for i in range(0,10):
    print "Main running"
    time.sleep(1)
  print "Main terminated"
