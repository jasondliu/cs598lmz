import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

database_path = "../database/"
db = Database(database_path)

def main():
    print(db.list_Species())

if __name__ == "__main__":
    main()
