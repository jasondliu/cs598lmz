import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Rythm Bot | Public Release | 14th July 2018")

#initialize client
client = commands.Bot(command_prefix = "!")
client.remove_command('help')

#discord token
if os.path.isfile("token.txt"):
    f = open("token.txt","r")
    token = f.read()
    f.close()
    token = token.strip()
else:
    token = input("Please enter your discord bot token: ")
    f = open("token.txt", "w")
    f.write(token)
    f.close()

#login
@client.event
async def on_ready():
    print("\n" * 100)
    print("\n")
    print("\t\t\t\t\t\t    ____                                                 ")
    print("\t\t\t\t\t\t   / ___|___  _ __ ___  _ __ ___   __ _ _ __   __ _ ___  ")
    print("\
