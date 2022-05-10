fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
```

```
Traceback (most recent call last):
  File "python", line 4, in <module>
TypeError: code object argument required
```

For this particular example the error code is 1. So the correct message
is `"TypeError: code object argument required\n"`

## Usage

```
usage: run_test [-h] [--pure] [--type TYPE] [--python PYTHON] [--inputs INPUTS]
                test_file

Error Messages Tests Runner

positional arguments:
  test_file             File with tests to run

optional arguments:
  -h, --help            show this help message and exit
  --pure                Use pure Python
  --type TYPE, -t TYPE  Type of output file
  --python PYTHON, -p PYTHON
                        Python you want to run this tests with
  --inputs INPUTS, -i INPUTS
                        File with inputs for tests
```
