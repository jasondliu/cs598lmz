import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

def load_config():
    with open('config.json') as f:
        config = json.load(f)
    return config

config = load_config()

# conn = torndb.Connection(
#     '%s:%s' % (config['mysql_host'], config['mysql_port']),
#     config['mysql_database'],
#     user=config['mysql_user'],
#     password=config['mysql_password'],
#     charset='utf8mb4')


def main():
    if len(sys.argv) == 2:
        args = sys.argv[1]
        if args == '-u':
            print('')
    else:
        print("""
    Usage:
        -u: Update
        -o: Optimize
        """)

if __name__ == '__main__':
    main()
