import threading
# Test threading daemon
# def run(n):
#     print('task ', n)
#     time.sleep(2)
#     print('task ', n, 'done')
#
# t1 = threading.Thread(target=run, args=('t1',))
# t2 = threading.Thread(target=run, args=('t2',))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('main thread done')
# Test threading daemon
import asyncio
#
# async def get_html(url):
#     print('start get url')
#     await asyncio.sleep(2)
#     print('end get url')
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     tasks = [get_html('http://www.imooc.com') for i in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()
# Test asyncio


