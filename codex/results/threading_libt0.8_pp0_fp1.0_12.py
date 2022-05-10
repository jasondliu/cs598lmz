import threading
threading.stack_size(67108864)
import telnetlib
import time

from clientutils import Logger


class TelnetController:
    """
    Telnet operations
    """

    @staticmethod
    def TelnetLogin(ip, port, username, password, timeout=5):
        try:
            tn = telnetlib.Telnet(ip, port, timeout)
            tn.set_debuglevel(0)
            tn.read_until(b'Username:', timeout)
            tn.write(username.encode('ascii') + b'\n')
            tn.read_until(b'Password:', timeout)
            tn.write(password.encode('ascii') + b'\n')
            time.sleep(0.5)
            tn.read_very_eager()
            return tn
        except Exception as e:
            Logger.log('Failed to login telnet: ' + str(e))
            return None

    @staticmethod
    def TelnetLogout(tn):
        t
