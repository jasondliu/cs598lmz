fn = lambda: None
# Test fn.__code__.co_filename return value.
if (is_spyder):
  td = os.path.join(d, "tmp_td")
  tfn = os.path.join(td, "test_file.py")
  if (not os.path.isdir(td)):
    os.makedirs(td)
  with open(tfn, "w") as f:
    f.write("def a():\n  pass\n")
  import test_file
  test_file.a() # Makes fn.__code__.co_filename accessible.
  assert(os.path.isfile(tfn))
  assert(os.path.isfile(fn.__code__.co_filename))
  # Assert that test_file module resides in td directory.
  assert(td in fn.__code__.co_filename)
  os.remove(tfn)
  os.rmdir(td)
if (not is_spyder): # Test console output if not in spyder environment.
  print("code.co_filename is: " + fn
