from bz2 import BZ2Decompressor
BZ2Decompressor()

def get_data():
    return pd.read_csv('titanic.csv')


def decapitalize_persons(persons):
    count = 0
    for person in persons:
        person.decapitalize()
        count += 1
        if count % 10000 == 0:
            print(count)

def decapitalize_persons_for_loops(persons):
    count = 0
    for i, person in enumerate(persons):
        #p.decapitalize()
        count += 1
        if count % 10000 == 0:
            print(count)

def apply_decapitalize(persons):
    count = 0
    def decap(person):
        #person.decapitalize()
        if count % 10000 == 0:
            print(count)
        return person
    persons.apply(decap, axis=1)

def apply_decapitalize_col(persons):
    count = 0
    def decap(person):
        #person.decapitalize()
        if count % 10000 == 0
