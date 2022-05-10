fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

def caller():
    fn()

for i in range(1000000):
    caller()
```

```bash
python3 -m perf timeit -s "import test4" -- "test4.caller()"
```
## Memory leaks in Python

* Profiling is easy: using pympler
* Diagnosis is hard: tools like meliae, flamegraphs don't work
* Fixing is impossible: You don't know where to add clearances, and actually these leaks are not that critical in most cases

```bash
python3 -m pympler.tracker
```
```python
```

```bash
```
## Compile everything! Numba, Dask, other JIT compilers...

Pros: *speed*, *speed*, *speed*

Cons: *crashes*, *perturbations*, *speed*
## Understand how well a Python package is implemented

* Look at the code and run the unit tests
* Read the docs (even though they don't say anything useful)
* Read the tutorials (even if you don't understand
