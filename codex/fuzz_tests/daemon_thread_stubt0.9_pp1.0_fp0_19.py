import sys, threading

def run():
    threading.Timer(2.0, run).start()
    reload(ui_shows)
    reload(ui_select_shows)
    reload(ui_items)
    reload(ui_tv_shows)
    reload(ui_episodes)
    reload(ui_season)
    reload(ui_movie_db)
    reload(main_menu)
    reload(rpc)
