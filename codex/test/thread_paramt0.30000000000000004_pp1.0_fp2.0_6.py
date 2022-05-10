import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Threading!\n')).start()

# Python 3.4+
import sys, threading
threading.Thread(target=sys.stdout.write, args=('Threading!\n',)).start()

# Python 3.4+
import sys, threading
threading.Thread(target=sys.stdout.write, kwargs={'data': 'Threading!\n'}).start()

# Python 3.4+
import sys, threading
threading.Thread(target=sys.stdout.write, args=('Threading!\n',), daemon=True).start()

# Python 3.4+
import sys, threading
threading.Thread(target=sys.stdout.write, args=('Threading!\n',), daemon=False).start()

# Python 3.4+
import sys, threading
threading.Thread(target=sys.stdout.write, args=('Threading!\n',), daemon=True, name='threading').start()

# Python 3.4+
import sys
