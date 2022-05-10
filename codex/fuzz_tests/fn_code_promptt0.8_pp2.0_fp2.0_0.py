fn = lambda: None
# Test fn.__code__.co_filename
fn.__code__ = Attr(co_filename=None)
fn.__code__ = Attr(co_filename="")

# Test file opener
open(name=None)
open(name="", mode="")

# Test os.open
os.open(None)
os.open("")

# Test subprocess
subprocess.check_output(None, shell=False)
subprocess.check_output("", shell=True)

# Test runpy
runpy.run_module(mod_name="", alter_sys=None, run_name=None)
runpy.run_module("", alter_sys=0, run_name="")

# Test tokenize
tokenize.open(None)
tokenize.open("")
