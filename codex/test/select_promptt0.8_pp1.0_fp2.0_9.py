import select
# Test select.select, callbacks, and queue.Queue

def test(q):
	q.put('hello')

q = Queue.Queue()

select.select([], [], [], 1.0)
q.get()

select.select([], [], [], 1.0)
select.select([], [], [], 1.0)

select.select([], [], [], 1.0)
t = Thread(target=test, args=(q,))
t.start()
q.get()
t.join()

select.select([], [], [], 1.0)
assert q.empty()

class MyEvent:
	pass
evt = MyEvent()

class MyThread(Thread):
	def run(self):
		select.select([], [], [], 0.0)
		select.select([], [], [], 0.0)
