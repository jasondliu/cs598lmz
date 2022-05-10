import mmap
import os

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

class Action(Enum):
    LEVELLING = 1
    GRINDING = 2
    GRINDING_LV60 = 3
    MILITARY_SUPPLY_MISSIONS = 4
    CHAPTER_QUESTS_LV70 = 5
    CHAPTER_QUESTS_LV70_PT2 = 6

class Character(Enum):
    NOT_SET = 0
    MAIN_ALTICHIERI = 1
    ALTICHIERI = 3
    VALVEK = 5
    CONRAD = 6
    MASTER_CONRAD = 7
    CLAIRE = 8
    LIDIA = 10
    REINE = 11
    MASTER_REINE
