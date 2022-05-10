import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Discord Game Status & Presence")

print("\n")
print("Welcome to the Discord Game Status & Presence setup!")
print("We will use the developer portal at https://discord.com/developers")
print("to set up your info for your Discord Game Status!")
print("\n")

print("First, let's setup your Client ID and Client Secret.")
print("This will allow our program to use the Discord API.")

clientId = input("What is your Client ID? (Copy this as well) ")
clientSecret = input("What is your Client secret? (Copy this as well) ")

print("We will now generate you a refresh token.")
print("Sign in to the same Discord account you used to generate the")
print("Client ID and Client Secret.")

refreshToken = input("Enter your refresh token: ")

print("Now let's set up your activity.")

activityType = input("What activity type are you using? (1 = Playing, 2 = Streaming) ")

if (activityType == "1"):
    

