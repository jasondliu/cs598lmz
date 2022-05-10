fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__

reload(sys)
sys.setdefaultencoding('utf-8')


def read_sectors():
    global c
    global id_rec
    global N
    global sector
    global sector_dict
    global K

    csv_file = csv.reader(file('Sector.csv', 'rb'))
    for i, row in enumerate(csv_file):
        if i == 0:
            continue
        sec_id = int(row[0])
        sec_index = row[1]
        sec_name = row[2]

        sector_id[sec_index] = sec_id
        sector_dict[sec_id] = sec_name
        K = K + 1


def read_companies():
    global c
    global id_rec
    global N
    global sector
    global sector_dict
    global K
    global company

    csv_file = csv.reader(file('company.csv', 'rb'))
    for i, row in enumerate(csv_file):
        if i
