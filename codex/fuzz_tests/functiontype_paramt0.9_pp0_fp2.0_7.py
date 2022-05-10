from types import FunctionType
list(FunctionType(*create_command(['python2.7', '/usr/lib/pi-server/pi-server-cmd.py', 'get_uptime']).get_args()))

python_out = LocalCmd.subprocess_check_output2(['python2.7', '/usr/lib/pi-server/pi-server-cmd.py', 'get_uptime'])

import subprocess
subprocess.Popen(['python2.7', '/usr/lib/pi-server/pi-server-cmd.py', 'get_uptime'])
subprocess.Popen(['python2.7', '/usr/lib/pi-server/pi-server-cmd.py', 'hibernate'])
subprocess.Popen(['python2.7', '/usr/lib/pi-server/pi-server-cmd.py', 'shutdown'])
subprocess.Popen(['python2.7', '/usr/lib/pi-server/pi-server-cmd.py', 'reboot'])
sys.executable
LocalCmd.subprocess_check_output2(['python2
