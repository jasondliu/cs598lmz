fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
sys.meta_path.append(fn)

import sys
print(sys.meta_path)

## [<class 'importlib._bootstrap_external.BuiltinImporter'>, <class 'importlib._bootstrap_external.FrozenImporter'>, <class 'importlib._bootstrap_external.PathFinder'>]

# 继续
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
sys.meta_path.insert(0, fn)

import sys
print(sys.meta_path)

## [<function <lambda> at 0x7f817dffb400>, <class 'importlib._bootstrap_external.BuiltinImporter'>, <class 'importlib._bootstrap_external.FrozenImporter'>, <class 'importlib._bootstrap_external.PathFinder'>]


##############
# 子弹
# 发
