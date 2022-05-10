import types
types.SimpleNamespace(**{'a': 1, 'b': 2})

data = {k: getattr(data, k) for k in data.__slots__}
data = vars(data)

data = {**data, **{'test': 1}}

data = json.loads(json.dumps(data, cls=TypeEncoder))

pickle.dump(data, open('/home/konrad/PycharmProjects/DDD_PY/test/test_data', 'wb'))
data = pickle.load(open('/home/konrad/PycharmProjects/DDD_PY/test/test_data', 'rb'))

print(data)



# todo duplicated class
class Person(dd.AggregateRoot):
    pass


person = Person()
person.publish(PersonCreated(name='Konrad', age=32))

print(person.__dict__)

# person.publish(PersonUpdated(name='Konrad', age=32))
#
# print(person
