import select
# Test select.select
r, w, e = select.select([1], [1, 2], [], 10)
r, w, e # mousedown:init:r, mousedown:init:w, mousedown:init:e
r, w, e = select.select(['1f19d'], [], [], 10)
r, w, e # mousedown:error:r, mousedown:error:w, mousedown:error:e
r, w, e = select.select('1234', [], [], 10)
r, w, e # mousedown:error:r, mousedown:error:w, mousedown:error:e
# Test select.poll
p = select.poll()
p.poll(10) # mousedown:init:poll
p.poll([]) # mousedown:error:poll
p.poll((1, 2, 3)) # mousedown:error:poll
p.poll({'1': 2, '3': 4}) # mousedown:error:poll
w = select.poll()
