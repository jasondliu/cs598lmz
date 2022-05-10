fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__closure__ = ()

gis = []

for i in range(10000):
    gis.append(gi)
    gi = (i for i in gis)

fn()
</code>
This code fails with the following exception:
<code>Traceback (most recent call last):
  File "sandbox.py", line 13, in &lt;module&gt;
    fn()
  File "sandbox.py", line 6, in &lt;lambda&gt;
    fn = lambda: None
  File "sandbox.py", line 6, in &lt;module&gt;
    fn = lambda: None
  File "sandbox.py", line 6, in &lt;module&gt;
    fn = lambda: None
  File "sandbox.py", line 6, in &lt;module&gt;
    fn = lambda: None
  File "sandbox.py", line 6, in &lt;module&gt;
    fn = lambda: None
  File "sandbox.py", line 6, in &lt;module&gt
