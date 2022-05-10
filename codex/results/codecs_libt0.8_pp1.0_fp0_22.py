import codecs
codecs.register_error("strict", codecs.ignore_errors)
condir = os.path.join(os.path.dirname(__file__), "node_modules", "prepor", "data")
CON = json.load(open(os.path.join(condir, "con2.json")))
CON_SET = set(CON.keys())
#CON_SET.update(set(CON.values()))
USERS = None


def init_users():
    global USERS
    if USERS is not None:
        return
    print "Loading users"
    USERS = {}
    with open(os.path.join(condir, "users.tsv")) as f:
        for line in f:
            userid, name = line.decode("utf8").strip().split("\t")
            USERS[userid] = name


def _get_links(html):
    for link in re.findall(r'<link.*?>', html, re.I | re.M | re.S):
        href = re.search(r'
