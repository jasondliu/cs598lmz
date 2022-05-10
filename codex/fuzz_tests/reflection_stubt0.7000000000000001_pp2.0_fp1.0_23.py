fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(gi.gi_code)
sys.modules['__main__'].c = fn

import dill
dill.dumps(fn)
</code>
Here is the error message:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    dill.dumps(fn)
  File "/usr/local/lib/python3.5/dist-packages/dill/dill.py", line 189, in dumps
    dump(obj, file, protocol, byref, fmode, recurse, strictio)
  File "/usr/local/lib/python3.5/dist-packages/dill/dill.py", line 185, in dump
    pik.dump(obj)
  File "/usr/local/lib/python3.5/dist-packages/dill/dill.py", line 586, in save
    StockPickler.save(self, obj)
  File "/usr/lib/python3.5/pickle.py", line 437, in save
    self
