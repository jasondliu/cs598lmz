import ctypes
ctypes.windll.user32.LockWorkStation()
</code>
This doesn't work when I run it on a test computer. What am I missing?


A:

To run this using an account that is not in the Administrators group you need to provide an additional parameter to <code>openas</code> to duplicate the PrimaryToken using <code>TokenPrimary</code>.
The elevated prompt will have a lower (impersonation) token and you will not be able to call <code>LockWorkStation</code> from the impersonation token from python.
<code>import sys
import ctypes
import win32api
import win32con
import win32com.shell.shell as shell

ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)

   
