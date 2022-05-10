import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello World\n')).start()

# Python 3.4+
import threading
threading.Thread(target=print, args=('Hello World',), daemon=True).start()

# Python 3.5+
import asyncio
asyncio.run(print('Hello World'))

# Python 3.6+
import asyncio
asyncio.run(print('Hello World'))

# Python 3.7+
import asyncio
asyncio.run(print('Hello World'))

# Python 3.8+
import asyncio
asyncio.run(print('Hello World'))

# Python 3.9+
import asyncio
asyncio.run(print('Hello World'))

# Python 4.0+
import asyncio
asyncio.run(print('Hello World'))

# Python 5.0+
import asyncio
asyncio.run(print('Hello World'))

# Python 6.0+
import asyncio
asyncio.run(print('Hello World'))

# Python 7
