from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("QQQQQQQ", little=True)
s.unpack("A")
s.pack("f" * 13, *range(13))
```

```python
# bin/pybench_struct.py
from test.libregrtest.runtest import runtest_inner
runtest_inner(None, 'test_struct.py', True)
```

## Compare

```shell
bin/python bench_struct_pypy.py
bin/python pybench_struct.py --output struct_output_pypy.txt

bin/python bench_struct_cpython.py
bin/python pybench_struct.py --output struct_output_cpython.txt

```

```shell
# Compare pybench result
bin/python pybench_compare.py --python='bin/python bin/pybench_struct.py --output struct_output_cpython.txt
bin/python bin/pybench_struct.py --output struct_output_pypy.txt'
```

## Result
