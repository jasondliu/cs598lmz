import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from a thread\n")).start()

def function():
  while True:
   time.sleep(0.0001)

print("Hello World!")
t1 = threading.Thread(target=function)
t1.start()

print("threads running:", threading.activeCount())
`

func (s *vmSuite) TestThreading(c *C) {
	out, err := s.vm.Run(threadTest)
	c.Check(err, Equals, nil)
	lines := strings.SplitN(out, "\n", 4)
	c.Check(lines[0], Equals, "Hello from a thread")
	c.Check(lines[1], Equals, "Hello World!")
	c.Check(lines[2], Equals, "threads running: 3")
	c.Check(len(lines), Equals, 4)
}

const childTest = `
import time
#function to be called by child thread
def child():
   time.sleep(0.0001)
   print("
