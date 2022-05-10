import sys, threading

def run():
    asyncio.set_event_loop(asyncio.new_event_loop())
    cl = Cryptomator(*sys.argv[1:])
    result = cl.main()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(cl.event_loop())
    loop.close()

threading.stack_size(128 * 1024 * 1024)
t = threading.Thread(target=run)
t.start()
t.join()
