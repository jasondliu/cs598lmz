import threading
threading._DummyThread._Thread__stop = lambda x: 42

from zope.site.hooks import setSite, setHooks


# Search for a task file
if len(sys.argv) != 2:
    print("usage: buildouttest.py task-file")


task_file = sys.argv[1]

if not os.path.isfile(task_file):
    print("ERROR: task-file %s cannot be found" % task_file)
    sys.exit(1)

task_file_contents = open(task_file, "r").readlines()

task_file_contents = "".join([x for x in task_file_contents
                              if x.strip() and not x.strip().startswith("#")])

try:
    task = eval(task_file_contents)
except:
    print("Could not understand task-file %s" % task_file)
    sys.exit(1)

relative = task["relative"]

setHooks()
reset_logging_settings()

