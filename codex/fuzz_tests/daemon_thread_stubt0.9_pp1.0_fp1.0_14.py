import sys, threading

def run():
  sys.stdout.write("Test: cleaning output directory...")
  sys.stdout.flush()
  shutil.rmtree(BASEDIR + "output", True)
  os.mkdir(BASEDIR + "output")
  print " done."

  sys.stdout.write("Test: collecting test modules...")
  sys.stdout.flush()
  tests = []
  names = []
  for t in (os.listdir(BASEDIR + "tests")):
    if t[-3:] != ".py":
      continue
    t = t[:-3]
    tests.append(importlib.import_module("tests." + t))
  print " done (" + str(len(tests)) + " test modules)"

  assert len(tests) > 0
  
  for t in tests:
    sys.stdout.write("Test: running " + t.__name__ + "...")
    sys.stdout.flush()
    t.main()
    print " done."

# Make sure basepath is properly applied
import os.path

