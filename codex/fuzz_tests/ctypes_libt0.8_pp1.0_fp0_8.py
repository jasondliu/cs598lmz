import ctypes
ctypes.windll.kernel32.SetConsoleTitleA("LOLHACK IS ON VAC")
print("Loading...")
time.sleep(5)
say = wincl.Dispatch("SAPI.SpVoice")
say.Speak("You are now using Lolhack")

ctypes.windll.kernel32.SetConsoleTitleA("LOLHACK")

#Clear the console
os.system("cls")

api_key = "RGAPI-edf40b2c-c1be-4b9e-b4ad-4a4b4a4b4b4b"
region = "na1"

username = input("Summoner: ")
username = username.lower()
username = username.replace(" ", "")
username = username.replace("'", "")
url = "https://" + region + ".api.riotgames.com/lol/summoner/v3/summoners/by-name/" + username + "?api_key=" + api_key
output = requests.get(url)
summoner = output.json()

try:
