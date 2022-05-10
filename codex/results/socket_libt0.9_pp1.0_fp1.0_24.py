import socket
import argparse
import ssl
import os
import re
import ctypes
import ctypes.wintypes
import csv

import config
import win_spotify_util
import spotify_util
import spotify_terminal
import model
import spotify_api
import spotify_ui_event
import spotify_cache
import spotify_token


def main():
    os.system(["clear", "cls"][os.name == "nt"])
    print ("Welcome to spotify-terminal")
    print ("This is a proof of concept, it is still in development and some things might not work yet.")
    if config.SPECIFIC_TRACK:
        result = spotify_api.get_track_information(config.SPECIFIC_TRACK)
        print(result)
    if config.SPECIFIC_ARTIST:
        result = spotify_api.get_artist_information(config.SPECIFIC_ARTIST)
        for track in result:
            print(track)


if __name__ == "__main__":
    main()
