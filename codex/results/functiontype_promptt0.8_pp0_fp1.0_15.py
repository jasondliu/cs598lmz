import types
# Test types.FunctionType

def decorator(func):
    """decorator"""
    return func


@decorator
def f(x):
    """f"""
    return x


def g():
    """g"""
    pass

print(f.__name__, f.__doc__, f.__wrapped__, sep = "\n")
print(g.__name__, g.__doc__, g.__wrapped__, sep = "\n")
print(types.FunctionType.__module__)
print()

# Test workflow.workflow
import workflow

# Test workflow.fileInFileList
filelist = workflow.fileInFileList("dummy", ["dummy1", "dummy2"])
print(filelist, len(filelist))
print()

# Test workflow.fileInFileList
filelist = workflow.fileInFileList("dummy2", ["dummy1", "dummy2"])
print(filelist, len(filelist))
print()

# Test workflow.getFile
print(workflow.getFile("dummy"))
print
