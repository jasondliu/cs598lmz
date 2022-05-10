fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that the frame is not leaked.
import gc
gc.collect()

# Test that the frame is not leaked when the generator is created from a
# function defined in a different module.
fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
gc.collect()

# Test that the frame is not leaked when the generator is created from a
# function defined in a different module and a __del__ method is present.
import sys
import os

# Create a new module.
modname = 'mod'
modfile = modname + '.py'
with open(modfile, 'w') as f:
    f.write("def f(): yield 1\n")

# Import the module.
import importlib
mod = importlib.import_module(modname)

# Create a new function from the generator defined in the module.
fn = lambda: None
fn.__code__ = mod.f()
fn()

# Remove the module.
os.remove(modfile)
del sys.modules[
