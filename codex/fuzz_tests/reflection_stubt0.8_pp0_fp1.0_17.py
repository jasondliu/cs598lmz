fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
a = fn()  # yields `gi` as __code__ for a frame
type(a)  # => generator
```

## Install

```sh
pip install -r requirements.txt
```

`purescipy` should be installed with `pip` on both Python2 and Python3.

```sh
python setup.py install
```

## Run

```sh
python test.py
```

## Build Documentation

```sh
cd docs
sphinx-build -b html ./ _build
```
