import signal
# Test signal.setitimer()
signal.alarm(10) # set the alarm in 10 seconds


# Test the combination of uvloop and aiohttp

# aiohttp gets stuck in an infinite loop on macOS
# https://github.com/aio-libs/aiohttp/issues/1411
# import uvloop
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# import nest_asyncio
# nest_asyncio.apply()
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://python.org/')
        print(html)

asyncio.run(main())
