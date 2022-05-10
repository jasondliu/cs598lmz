from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda').__code__.co_consts)

# Output:
# [None, '<lambda>', 0, '<code object <lambda> at 0x7f8d3e3d3b70, file "<stdin>", line 1>']
```

## How to run the tests

```bash
python3 -m unittest discover -s tests -p '*_test.py'
```

## How to run the linter

```bash
pip install pylint
pylint --rcfile=pylint.rc lambda_function.py
```

## How to run the formatter

```bash
pip install black
black lambda_function.py
```
