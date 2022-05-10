import codecs
codecs.register_error("GT", codecs.ignore_errors)
import zipfile
import sqlite3

from src.lib.utils import get_db_path


def get_database():
    try:
        conn = sqlite3.connect(get_db_path())
        return conn
    except Exception as e:
        print('Unable to open database')
        print(e)


def get_teams():
    teams = []
    conn = get_database()
    c = conn.cursor()
    c.execute('select team_id, team.name, team.country, team.tla, team.crest_url, team.founded , stadium.name, stadium.address, stadium.capacity, stadium.area, team.source\
                from team, stadium\
                where team.stadium_id = stadium.stadium_id')
    for team in c:
        teams.append(team)
    return teams


def get_squads():
    squads = []
    conn = get_database()
    c = conn.cursor()
    c.execute('select ts.team_
