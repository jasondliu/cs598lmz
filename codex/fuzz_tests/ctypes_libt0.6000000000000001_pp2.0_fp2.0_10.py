import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Dota2 Replay Renamer")

# Define global variables

# Game mode
#
# 1 - None
# 2 - All Pick
# 3 - Captains Mode
# 4 - Random Draft
# 5 - Single Draft
# 6 - All Random
# 7 - Intro
# 8 - Diretide
# 9 - Reverse Captains Mode
# 10 - The Greeviling
# 11 - Tutorial
# 12 - Mid Only
# 13 - Least Played
# 14 - New Player Pool
# 15 - Compendium Matchmaking
# 16 - Captains Draft
# 17 - Balanced Draft
# 18 - Ability Draft
# 19 - Event
# 20 - All Random Death Match
# 21 - 1v1 Mid
# 22 - Ranked Matchmaking
# 23 - Turbo
game_mode = {
    1: "None",
    2: "All Pick",
    3: "Captains Mode",
    4: "Random Draft",
    5: "Single Draft",
    6: "All Random",
    7: "Intro",
    8: "Diretide",
   
