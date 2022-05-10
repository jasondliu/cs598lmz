import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

cursor = con.cursor()
cursor.execute('SET NAMES utf8mb4')
cursor.execute("SET CHARACTER SET utf8mb4")
cursor.execute("SET character_set_connection=utf8mb4")


with open('ks3000.txt') as f:
    ks = f.read().splitlines()

with open('en3000.txt') as f:
    en = f.read().splitlines()


def insert_data(table, word, translation, date):
    sql = "INSERT INTO {} (word, translation, date) VALUES (%s, %s, %s)".format(table)
    val = (word, translation, date)
    cursor.execute(sql, val)
    con.commit()
    print("{} data inserted".format(word))


date = datetime.datetime.now().date()
for i, k in enumerate(ks):
    try:
        insert
