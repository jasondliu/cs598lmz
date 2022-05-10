import sys, threading

def run():

  try:
    while 1:
      pass
  except SystemExit:
    return

  return

thread = threading.Thread(target=run)
thread.daemon = True
thread.start()

thread.join()  # Wait for it to start (test only)

"""

test.run_sconsign(None, python, arguments="-f SConstruct.1")

test.pass_test()

# Local Variables:
# tab-width:4
# indent-tabs-mode:nil
# End:
# vim: set expandtab tabstop=4 shiftwidth=4:
