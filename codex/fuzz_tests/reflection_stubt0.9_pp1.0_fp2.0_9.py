fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
# pycs
#for pyc in glob.glob("*.pyc"):
#    py_modname = pyc.rsplit(".", 1)[0]
#    if not os.path.exists(py_modname + ".py"):
#        print("Removing orphan .pyc file:", pyc)
#        os.unlink(pyc)

# __pycache__
for pyc in glob.glob("**/__pycache__", recursive=True):
    py_modname = pyc.rsplit(".", 1)[0]
    if not os.path.exists(py_modname + ".py"):
        print("Removing orphan .pyc file:", pyc)
        shutil.rmtree(pyc)

# rest useless
for pyc in glob.glob("*.pyc"):
    py_modname = pyc.rsplit(".", 1)[0]
    if not os.path.exists(py_modname + ".py"):
        print("Removing orphan
