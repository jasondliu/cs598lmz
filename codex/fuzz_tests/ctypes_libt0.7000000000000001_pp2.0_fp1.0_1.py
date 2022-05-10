import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Minecraft Server Manager")

import core.commands as commands
import core.db as db
import core.log as log
import core.player as player
import core.server as server
import core.settings as settings
import core.update as update
import core.updater as updater
import core.utils as utils

def init():
    settings.load()
    log.init()
    log.info("Logging initialized")
    db.init()
    log.info("Database initialized")
    player.init()
    log.info("Player manager initialized")
    server.init()
    log.info("Server manager initialized")

def main():
    init()
    utils.clearScreen()
    utils.printBanner()
    log.info("Minecraft Server Manager started")
    print("")
    print("Type 'help' to list all commands")
    print("")
    command = input("MSM> ")
    while command != "exit":
        if command:
            commands.execute(command.split())
            command
