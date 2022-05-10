import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("WoW Packet Viewer")
print(Fore.WHITE + Style.BRIGHT + "WoW Packet Viewer")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Port to listen on.", required=True, type=int)
    parser.add_argument("-d", "--database", help="Path to the database file.", required=False, type=str)
    args = parser.parse_args()
    port = args.port
    if args.database:
        print(Fore.GREEN + Style.BRIGHT + "Loading existing database...")
        try:
            update = True
            db = MySQLdb.connect(host="localhost", user="wowviewer", passwd="password", db="wowpacket")
            cursor = db.cursor()
            cursor.execute("DELETE FROM packets")
            db.commit()
            f = open(args.database, "r")
            for line in f:
                if line[0] == "#":
