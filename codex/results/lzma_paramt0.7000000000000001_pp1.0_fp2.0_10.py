from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self, length=None: bytes()

import os
if os.getenv('BOT_TOKEN') is None:
    import config

TOKEN = os.getenv('BOT_TOKEN')
bot = commands.Bot(command_prefix='&')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name='fping')
async def fping(ctx):
    url = 'http://www.wegottickets.com/searchresults/page/1/all'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            response = await resp.read()

    soup = bs4.BeautifulSoup(response, 'html.parser')
    events = soup.find_all('li', class_='event')

    if events is None:
        await ctx.send('No events found')
        return

    await ctx.send('Events found: ' + str(len(events)))


