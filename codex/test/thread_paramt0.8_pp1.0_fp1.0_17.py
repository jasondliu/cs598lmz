import sys, threading
threading.Thread(target=lambda: sys.stdout.write('Hello from a thread!\n')).start()
print('Hello from the main thread!')

# import asyncio
# async def f():
#     print('Hello from a coroutine!')
    
# loop = asyncio.get_event_loop()
# loop.run_until_complete(f())
# loop.close()

# from concurrent.futures import ThreadPoolExecutor
# import time
# def f(i):
#     time.sleep(0.5)
#     return i**2

# with ThreadPoolExecutor(max_workers=10) as exe:
#     results = exe.map(f, range(10))
#     for i, result in enumerate(results):
#         print(i, result)

# import xmlrpc.client
# proxy = xmlrpc.client.ServerProxy('http://localhost:9000')
# proxy.echo('echo')

# import Pyro4
# uri = input("enter the object uri: ").strip()
# ro = Pyro4.Proxy(uri
