import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("CBL Bot: Console")

CONFIG = json.load(open(r"config\config.json"))

if CONFIG["debug"]:
    bot = commands.Bot(command_prefix='$')
else:
    bot = commands.Bot(command_prefix=CONFIG["command_prefix"])

@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def invite(ctx):
    embed = discord.Embed(title='CBL Bot', description='You can invite me to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=743420285560461322&permissions=8&scope=bot)', color=0x00ff00)
    await ctx.send(embed=embed)

@bot.command()
async def support(ctx):
    embed = discord.
