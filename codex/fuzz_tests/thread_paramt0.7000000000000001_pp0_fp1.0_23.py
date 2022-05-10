import sys, threading
threading.Thread(target=lambda: sys.stdout.write("Hello from a thread!\n")).start()

import asyncio
asyncio.get_event_loop().run_until_complete(hello())
</code>

