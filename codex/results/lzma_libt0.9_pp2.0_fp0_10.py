import lzma
lzma.__file__ 
```

```
>>> import lzma
>>> print(lzma.__file__)
/Users/luoyuhui/anaconda3/lib/python3.7/lzma.py
```

### 当module OSError: cannot load module 'lzma'时 

```shell
pip install pyliblzma
```
供参考：https://github.com/python-pillow/Pillow/issues/2087

# 常见问题

## There are two instances of lzma.py on the path:

```shell
$ egrep -rn  'lzma.py' /Users/luoyuhui/anaconda3
/Users/luoyuhui/anaconda3/envs/py3/lib/python3.6/site-packages/ipywidgets/widgets/tests/test_utils.py:18:import lzma
/Users/luoyuhui/an
