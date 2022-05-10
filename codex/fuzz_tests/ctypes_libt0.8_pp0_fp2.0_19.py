import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

def run_script(script_path, args=[], ret_stdout=False, ret_stderr=False, env=None, username=None, password=None, working_dir=None, creationflags=0, wait=False):
  stdout = None
  stderr = None
  
  if ret_stdout:
    stdout = subprocess.PIPE
  
  if ret_stderr:
    stderr = subprocess.PIPE
  
  if wait:
    creationflags = creationflags | subprocess.CREATE_NEW_CONSOLE
  
  if os.path.splitext(script_path)[1].lower() == '.py':
    args = ['python.exe'] + [script_path] + args
    script_path = 'python.exe'
  
  if env is not None:
    env['PATH'] = os.environ['PATH']
    env['PYTHONPATH'] = os.environ['P
