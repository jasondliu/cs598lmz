import sys, threading
threading.Thread(target=lambda: sys.stdout.write('py')).start()
threading.Thread(target=lambda: sys.stderr.write('th')).start()

# Python 3
# >>> import sys, threading
# >>> threading.Thread(target=lambda: sys.stdout.write('py')).start()
# >>> threading.Thread(target=lambda: sys.stderr.write('th')).start()
# pt
# yh
# >>>
#
# Python 2
# >>> import sys, threading
# >>> threading.Thread(target=lambda: sys.stdout.write('py')).start()
# >>> threading.Thread(target=lambda: sys.stderr.write('th')).start()
# pt
# yh
# >>>

# 3.2
# >>> import sys
# >>> print(sys.stdout)
# <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF-8'>
# >>> print(sys.stderr)
# <_io.TextIOWrapper name='<st
